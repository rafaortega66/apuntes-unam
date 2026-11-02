#!/usr/bin/env python3
"""Experimento 3 (+2 pt): pagina web con un control deslizante para el foco.

Solo biblioteca estandar (igual que en la Practica 6). Abrir desde otro equipo
de la misma red en http://<ip-de-la-pi>:8080
    GET  /         -> pagina con el control
    GET  /status   -> JSON con la potencia pedida y la real
    POST /power    -> cuerpo JSON {"power": 0-100}
Uso: python3 exp3_web.py [--port 8080] [--simulate]
"""
import argparse
import json
import signal
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import p7_i2c

PAGE = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Foco - Practica 7</title>
<style>
 body{font-family:system-ui,sans-serif;max-width:480px;margin:2rem auto;padding:0 1rem;
      background:#111;color:#eee}
 h1{font-size:1.3rem} input[type=range]{width:100%;height:2.5rem}
 .big{font-size:3rem;font-weight:700;text-align:center;margin:.5rem 0}
 #bulb{width:120px;height:120px;border-radius:50%;margin:1rem auto;
       box-shadow:0 0 40px #000;transition:background .2s,box-shadow .2s}
 table{width:100%;border-collapse:collapse;margin-top:1rem}
 td{padding:.3rem;border-bottom:1px solid #333} td:last-child{text-align:right}
 .err{color:#f77}
</style></head><body>
<h1>Practica 7 &mdash; Brillo del foco incandescente</h1>
<div id="bulb"></div>
<div class="big"><span id="val">0</span> %</div>
<input id="sl" type="range" min="0" max="100" step="1" value="0">
<table>
 <tr><td>Potencia pedida</td><td id="req">-</td></tr>
 <tr><td>Retardo de disparo</td><td id="dly">-</td></tr>
 <tr><td>Angulo de disparo &alpha;</td><td id="alp">-</td></tr>
 <tr><td>Frecuencia medida</td><td id="frq">-</td></tr>
 <tr><td>Potencia real (Ec. 3)</td><td id="pr">-</td></tr>
 <tr><td>V<sub>o</sub>/V<sub>RMS</sub></td><td id="vr">-</td></tr>
</table>
<p id="msg"></p>
<script>
const sl=document.getElementById('sl'), val=document.getElementById('val');
let timer=null;
function paint(s){
  document.getElementById('req').textContent=s.requested.toFixed(1)+' %';
  document.getElementById('dly').textContent=s.delay_ms.toFixed(3)+' ms';
  document.getElementById('alp').textContent=s.alpha_deg.toFixed(1)+'°';
  document.getElementById('frq').textContent=s.freq_hz.toFixed(2)+' Hz';
  document.getElementById('pr').textContent=s.power_pct.toFixed(1)+' %';
  document.getElementById('vr').textContent=s.vo_vrms_pct.toFixed(1)+' %';
  const k=s.power_pct/100, b=document.getElementById('bulb');
  b.style.background=`rgb(${60+195*k|0},${50+170*k|0},${20+60*k|0})`;
  b.style.boxShadow=`0 0 ${10+90*k|0}px rgba(255,200,80,${k})`;
}
function msg(t){const m=document.getElementById('msg');m.textContent=t;m.className=t?'err':'';}
async function send(){
  try{
    const r=await fetch('/power',{method:'POST',headers:{'Content-Type':'application/json'},
                                  body:JSON.stringify({power:+sl.value})});
    const s=await r.json(); if(!r.ok) throw new Error(s.error); paint(s); msg('');
  }catch(e){msg('Error: '+e.message);}
}
sl.addEventListener('input',()=>{val.textContent=sl.value;clearTimeout(timer);timer=setTimeout(send,120);});
async function poll(){
  try{const r=await fetch('/status');const s=await r.json();if(!r.ok) throw new Error(s.error);paint(s);msg('');}
  catch(e){msg('Error: '+e.message);}
}
fetch('/status').then(r=>r.json()).then(s=>{if(s.requested!==undefined){sl.value=Math.round(s.requested);
  val.textContent=sl.value;paint(s);}});
setInterval(poll,2000);
</script></body></html>
"""

lock = threading.Lock()   # el bus I2C no se comparte entre hilos a la vez


class SimulatedArduino:
    """Para probar la pagina sin hardware (--simulate)."""
    def __init__(self):
        self.p = 0.0

    def write_power(self, p):
        self.p = p

    def read_status(self):
        import math
        # misma tabla que el Arduino
        tabla = [0.000, 2.060, 2.696, 3.157, 3.538, 3.874, 4.179, 4.464, 4.734, 4.993,
                 5.245, 5.493, 5.738, 5.984, 6.232, 6.487, 6.750, 7.030, 7.334, 7.688, 8.203]
        if self.p <= 0.5:
            d = 0.0
        else:
            pos = (100 - self.p) / 5
            i = min(int(pos), 19)
            d = max(0.150, tabla[i] + (pos - i) * (tabla[i + 1] - tabla[i]))
        return p7_i2c.describe(self.p, d, 8.333)


backend = p7_i2c


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype='application/json'):
        data = body.encode() if isinstance(body, str) else body
        self.send_response(code)
        self.send_header('Content-Type', ctype + '; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)

    def _json(self, code, obj):
        self._send(code, json.dumps(obj))

    def do_GET(self):
        if self.path == '/':
            self._send(200, PAGE, 'text/html')
        elif self.path == '/status':
            try:
                with lock:
                    st = backend.read_status()
                self._json(200, st)
            except OSError as e:
                self._json(503, {'error': 'I2C: {}'.format(e)})
        else:
            self._json(404, {'error': 'not found'})

    def do_POST(self):
        if self.path != '/power':
            return self._json(404, {'error': 'not found'})
        try:
            n = int(self.headers.get('Content-Length', 0))
            if n > 1024:
                raise ValueError
            pwr = float(json.loads(self.rfile.read(n))['power'])
            if not 0 <= pwr <= 100:
                raise ValueError
        except (ValueError, KeyError, TypeError, json.JSONDecodeError):
            return self._json(400, {'error': 'power debe ser un numero entre 0 y 100'})
        try:
            with lock:
                backend.write_power(pwr)
                st = backend.read_status()
            self._json(200, st)
        except OSError as e:
            self._json(503, {'error': 'I2C: {}'.format(e)})

    def log_message(self, fmt, *args):   # silencia el log por peticion
        pass


def main():
    global backend
    ap = argparse.ArgumentParser()
    ap.add_argument('--port', type=int, default=8080)
    ap.add_argument('--simulate', action='store_true')
    args = ap.parse_args()
    if args.simulate:
        backend = SimulatedArduino()
    srv = ThreadingHTTPServer(('0.0.0.0', args.port), Handler)

    def on_sigterm(signum, frame):        # kill/systemd tambien apagan el foco
        raise KeyboardInterrupt
    signal.signal(signal.SIGTERM, on_sigterm)
    print('Sirviendo en http://0.0.0.0:{}  (Ctrl+C para salir)'.format(args.port))
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        try:
            with lock:
                backend.write_power(0)      # deja el foco apagado al salir
        except OSError:
            pass


if __name__ == '__main__':
    main()
