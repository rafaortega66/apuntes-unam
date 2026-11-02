/*
 * Practica 7 - Modulacion de potencia de una lampara incandescente
 * Arduino UNO como esclavo I2C (0x0A) de la Raspberry Pi.
 *
 * - D2 (INT0): salida del detector de cruce por cero (4N25, pull-up 10k).
 * - D3       : senal "Dimmer" hacia el MOC3021 (R3 = 470 ohm).
 * - A4/A5    : SDA/SCL hacia la Raspberry Pi (Tabla 2 del manual).
 *
 * En lugar de delayMicroseconds() en loop() (Apendice A), el retardo de
 * disparo lo mide el Timer1 en hardware: el cruce por cero arranca el timer,
 * COMPA enciende el TRIAC y COMPB apaga el pulso de gate 20 us despues.
 * Asi el disparo no depende de lo que este haciendo loop() ni del I2C.
 *
 * Protocolo I2C:
 *   Escritura (Pi -> Arduino): 4 bytes, float little-endian = potencia 0-100 %.
 *   Lectura   (Arduino -> Pi): 12 bytes, 3 floats little-endian:
 *       [0] potencia solicitada (%)
 *       [1] retardo de disparo aplicado (ms despues del cruce por cero)
 *       [2] semiperiodo de linea medido entre cruces (ms; 8.333 a 60 Hz)
 *   Con [1] y [2] la Raspberry Pi calcula la potencia real (Experimento 2).
 */
#include <Wire.h>

#define I2C_SLAVE_ADDR 0x0A
#define ZXPIN          2      // INT0 en el UNO
#define TRIAC          3
#define BOARD_LED      13

#define TICKS_PER_US   2      // Timer1 con prescaler 8 a 16 MHz -> 0.5 us por tick
#define GATE_PULSE_US  20     // ancho del pulso al MOC3021
#define MIN_DELAY_US   150    // disparar antes casi no deja corriente de enganche
#define ZX_DEBOUNCE_US 6000   // ignora rebotes del detector dentro del mismo semiciclo

// Tabla 1 del manual (60 Hz, pasos de 5 %): tiempo de disparo en ms
// para 100, 95, 90, ..., 5, 0 %.
const float FIRE_TABLE_MS[21] = {
  0.000, 2.060, 2.696, 3.157, 3.538, 3.874, 4.179,
  4.464, 4.734, 4.993, 5.245, 5.493, 5.738, 5.984,
  6.232, 6.487, 6.750, 7.030, 7.334, 7.688, 8.203
};

// Estado compartido con interrupciones
volatile float    requestedPower = 0;     // lo escribe el handler de I2C
volatile uint16_t fireTicks      = 0;     // 0 = lampara apagada
volatile uint32_t lastZxMicros   = 0;
volatile uint32_t halfPeriodUs   = 8333;
volatile bool     newRequest     = false;

float appliedDelayMs = 0;                 // lo que realmente se programo
byte  replyBuffer[12];

// Interpolacion lineal en la Tabla 1: potencia (%) -> retardo (us).
// Devuelve 0 si la lampara debe ir apagada.
uint16_t powerToDelayUs(float p) {
  if (p <= 0.5) return 0;                 // apagada
  if (p > 100) p = 100;
  float pos = (100.0 - p) / 5.0;          // indice fraccionario en la tabla
  int i = (int)pos;
  if (i >= 20) i = 19;
  float frac = pos - i;
  float ms = FIRE_TABLE_MS[i] + frac * (FIRE_TABLE_MS[i + 1] - FIRE_TABLE_MS[i]);
  uint16_t us = (uint16_t)(ms * 1000.0 + 0.5);
  if (us < MIN_DELAY_US) us = MIN_DELAY_US;
  return us;
}

void updateReply() {
  float r[3];
  noInterrupts();
  r[0] = requestedPower;
  uint32_t hp = halfPeriodUs;
  interrupts();
  r[1] = appliedDelayMs;
  r[2] = hp / 1000.0;
  memcpy(replyBuffer, r, sizeof(r));     // el AVR es little-endian, igual que '<f'
}

// ---------- Interrupciones ----------

void zxHandler() {
  uint32_t now = micros();
  uint32_t dt = now - lastZxMicros;
  if (dt < ZX_DEBOUNCE_US) return;
  lastZxMicros = now;
  if (dt < 20000) halfPeriodUs = dt;      // descarta el primer cruce tras un apagon

  digitalWrite(TRIAC, LOW);
  TCCR1B = 0;                             // detiene el timer del semiciclo anterior
  if (fireTicks == 0) return;             // 0 % -> no se dispara
  TCNT1  = 0;
  OCR1A  = fireTicks;
  OCR1B  = fireTicks + GATE_PULSE_US * TICKS_PER_US;
  TIFR1  = _BV(OCF1A) | _BV(OCF1B);       // limpia banderas pendientes
  TIMSK1 = _BV(OCIE1A) | _BV(OCIE1B);
  TCCR1B = _BV(CS11);                     // arranca con prescaler 8
}

ISR(TIMER1_COMPA_vect) {                  // fin del retardo: dispara el TRIAC
  digitalWrite(TRIAC, HIGH);
  digitalWrite(BOARD_LED, HIGH);
}

ISR(TIMER1_COMPB_vect) {                  // fin del pulso de gate
  digitalWrite(TRIAC, LOW);
  digitalWrite(BOARD_LED, LOW);
  TCCR1B = 0;                             // el TRIAC sigue conduciendo hasta el siguiente cruce
}

// ---------- I2C ----------

void i2c_received_handler(int count) {
  if (count != 4) {                       // descarta paquetes de otro tamano
    while (Wire.available()) Wire.read();
    return;
  }
  float f;
  byte *fp = (byte *)&f;
  for (byte i = 0; i < 4; ++i) fp[i] = (byte)Wire.read();
  if (f != f) return;                     // NaN
  if (f < 0) f = 0;
  if (f > 100) f = 100;
  requestedPower = f;
  newRequest = true;
}

void i2c_request_handler() {
  Wire.write(replyBuffer, sizeof(replyBuffer));
}

// ---------- Programa ----------

void setup() {
  pinMode(ZXPIN, INPUT);
  pinMode(TRIAC, OUTPUT);
  pinMode(BOARD_LED, OUTPUT);
  digitalWrite(TRIAC, LOW);

  TCCR1A = 0;                             // Timer1 en modo normal, detenido
  TCCR1B = 0;
  TIMSK1 = 0;

  Wire.begin(I2C_SLAVE_ADDR);
  Wire.onReceive(i2c_received_handler);
  Wire.onRequest(i2c_request_handler);

  attachInterrupt(digitalPinToInterrupt(ZXPIN), zxHandler, RISING);

  Serial.begin(57600);
  updateReply();
}

void loop() {
  static uint32_t lastPrint = 0;

  if (newRequest) {
    newRequest = false;
    noInterrupts();
    float p = requestedPower;
    interrupts();
    uint16_t us = powerToDelayUs(p);
    noInterrupts();
    fireTicks = us * TICKS_PER_US;        // max 8203 us * 2 = 16406 < 65535
    interrupts();
    appliedDelayMs = us / 1000.0;
    updateReply();
  }

  if (millis() - lastPrint >= 1000) {     // estado por el monitor serie
    lastPrint = millis();
    updateReply();                        // refresca el semiperiodo medido
    float r[3];
    memcpy(r, replyBuffer, sizeof(r));
    char a[10], b[10], c[10];
    dtostrf(r[0], 6, 2, a);               // el printf del AVR no soporta %f
    dtostrf(r[1], 6, 3, b);
    dtostrf(r[2], 6, 3, c);
    Serial.print(F("P = "));     Serial.print(a);
    Serial.print(F(" %  t = ")); Serial.print(b);
    Serial.print(F(" ms  T/2 = ")); Serial.print(c);
    Serial.println(F(" ms"));
  }
}
