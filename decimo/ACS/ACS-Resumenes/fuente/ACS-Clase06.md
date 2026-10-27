% materia: Arquitectura Cliente-Servidor
% titulo: Clase 6 · signal(), sus tres escenarios y procesos en foreground/background
% subtitulo: Arquitectura Cliente-Servidor · Mtro. Carlos Alberto Román Zamitiz · jueves 10 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Repaso de la Clase 5 (a la que no asistí)
- El Tema 2 (estados de un proceso y señales) arrancó en la Clase 5.
- **Huérfano:** si el padre muere antes, el PPID del hijo cambia a **1**: lo adopta init/systemd.
- **SIGCHLD:** el hijo la manda al padre al morir para que limpie la tabla de procesos. **17 en x86/ARM** (18 en otras; corrige lo reconstruido en la Clase 5).

## 2. man 7 signal
Sección *Signal numbering for standard signals*, columna **x86/ARM**:
| Señal | Número | Qué es |
|---|---|---|
| SIGINT | 2 | Ctrl+C; se ignora o maneja |
| SIGABRT | 6 | El proceso se aborta a sí mismo |
| SIGKILL | 9 | Matanza ineludible |
| SIGTERM | 15 | Terminación (p. ej. shutdown); se ignora o trata |
| SIGCHLD | 17 | Hijo → padre al terminar |

## 3. signal() y sus tres escenarios
Prototipo en `<signal.h>`: `void (*signal(int sig, void (*func)(int)))(int);`
| Escenario | Cómo | Efecto |
|---|---|---|
| 1. Ignorar | `signal(SIGINT, SIG_IGN);` | Ctrl+C no hace nada; `SIG_DFL` regresa al comportamiento nativo |
| 2. Manejar | `signal(SIGINT, manejador)` con prototipo `void f(int)` | v1: vuelve al `while(1)` y sigue vivo; v2: `exit(0)` en el manejador (o tras N veces con `static int cnt`) |
| 3. No capturable | `signal(SIGKILL, …)` regresa error | SIGKILL ("Avada Kedavra") no se ignora, bloquea ni maneja |
```
void manejador_senales(int sig) {
  if (sig == SIGINT) printf("Señal número %d recibida\n", sig);
}
int main() {
  signal(SIGINT, manejador_senales);
  while (1) { printf("En espera de Ctrl+C. PID: %d\n", getpid()); sleep(5); }
}
```

## 4. Foreground y background
- **Foreground:** atado a la terminal, recibe el teclado y la bloquea.
- **Background:** corre en tiempo compartido y libera la línea de comandos.
1. Ejecutar en primer plano.
2. **Ctrl+Z** → SIGTSTP, queda *Stopped*.
3. **bg** → sigue en segundo plano; muestra su número de trabajo (p. ej. [33]).
- `jobs` lista trabajos; **`fg %N`** lo trae al frente (Ctrl+C solo afecta al foreground).
- Si imprime con `printf()`, ensucia la terminal: redirigir a archivo o `/dev/null`.
!!! Huérfano vs. zombie (examen)
**Huérfano:** el padre muere primero; lo adopta PID 1 (o un reaper). **Zombie:** el hijo ya murió y el padre no procesó SIGCHLD ni limpió su entrada. Capturar señales y controlar procesos será requisito del proyecto final.

## Pendiente
- Sin clase martes 15 sep. Tarea 3 en la plataforma: calificación máxima si se entrega antes del jueves 17 sep; tarde vale menos.
- Próxima: procesos zombie y captura de SIGCHLD.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Números x86/ARM | INT 2, ABRT 6, KILL 9, TERM 15, CHLD 17 |
| signal() | Ignorar (SIG_IGN), manejar (`void f(int)`), o no se puede (SIGKILL) |
| SIG_DFL | Regresa al comportamiento por defecto |
| Ctrl+Z / bg / jobs / fg | Pausa / segundo plano / lista / primer plano |
| Huérfano | Padre muere primero → PPID 1 |
| Zombie | Hijo muerto sin que el padre lea SIGCHLD |
