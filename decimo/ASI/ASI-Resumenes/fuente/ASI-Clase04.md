% materia: Administración de Servicios de Internet
% titulo: Clase 4 · DHCP: DORA, componentes, seguridad e ISC vs. KEA
% subtitulo: Administración de Servicios de Internet · Mtro. Baldomero de Jesús Hernández Bañuelos (invitado) · lunes 7 sep 2026 · DHCP · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. DNS vs. DHCP
- **DNS:** traductor de nombres de dominio a IP (como la agenda del celular: guardamos nombres, no números).
- **DHCP:** **asigna y administra** las IPs. Sin él, cada IP se configura a mano.
Error común: creer que el DNS asigna IPs.

## 2. Por qué automatizar
- Como las operadoras de Telmex que conectaban cables hasta que se automatizó: antes se necesitaban ingenieros (Cisco, 3Com) configurando IP por puerto.
- IoT: un hogar tiene 15, 20 o hasta 100 dispositivos; registrar MAC por MAC es inviable, más en una empresa.

## 3. Seguridad
| Amenaza | Qué hace |
|---|---|
| **DoS por agotamiento** (starvation) | Pedir IPs falsas hasta vaciar el pool |
| Inyección SQL + DoS | Instrucciones masivas; reiniciar el módem puede empeorarlo |
| **Rogue DHCP** | Servidor falso que reparte IPs maliciosas y redirige tráfico |
| Fuga por IP y DNS expuestos | Acceso a tráfico ajeno |
Defensas: **DMZ** ("campo minado" con alarmas), firewalls y **VPN** (túnel cifrado). Casos: Liverpool y Avante Textil, ~15 días antes.

## 4. Ventajas
- Sin bitácora manual nodo–puerto–IP; mapa de la topología y dominios de colisión.
- **Evita IPs duplicadas:** Rafael (mañana) e Iván (tarde) con la .100 asignada a mano chocarían.
- Escalabilidad y movilidad. Bancos y ejército pueden preferir IPs estáticas para reducir la superficie de ataque.

## 5. Proceso DORA
| Paso | Acción |
|---|---|
| **D**iscover | El cliente manda broadcast buscando servidor |
| **O**ffer | El servidor ofrece una IP libre |
| **R**equest | El cliente la solicita formalmente |
| **A**cknowledge | El servidor confirma y entrega IP, máscara, gateway y DNS |
**UNAM:** la red **RIU** era manual y daba IPs permanentes que no se liberaban → se saturaba. **PC Puma** usa DHCP: da IP al llegar y la libera al irse.

## 6. Los 6 componentes
| Componente | Qué es |
|---|---|
| **Ámbito** (scope) | Rango a entregar (192.168.1.100–200); la primera IP es la red, .255 broadcast, .1 gateway; por departamento |
| **Tiempo de concesión** | Cuánto conserva la IP el cliente |
| **Gateway** | Router de salida; **uno solo** (varios multiplican ×5 la superficie de ataque) |
| **Servidores DNS** | P. ej. 8.8.8.8 y 8.8.4.4 |
| **Reservas** | IP fija ligada a una MAC (equipos críticos) |
| **Exclusiones** | IPs del rango que no se entregan (127.0.0.1, estáticas) |
Error común: confundir reserva con exclusión.

## 7. Práctica: ISC DHCP y KEA DHCP
VM con tarjeta en **modo puente (Bridge)** o NAT, sudo e Internet.
```
sudo apt install isc-dhcp-server
sudo nano /etc/dhcp/dhcpd.conf     # red 192.168.1.0/24, rango .100-.200,
                                   # gateway .1, DNS 8.8.8.8 y 8.8.4.4
sudo systemctl restart isc-dhcp-server
sudo systemctl status isc-dhcp-server
sudo apt install kea-dhcp4-server  # usar 2.4, no 2.6
```
| | ISC DHCP | KEA DHCP |
|---|---|---|
| Estado | **Sin soporte desde fines de 2022** | Desarrollo activo |
| Arquitectura | Monohilo | **Multihilo** |
| Configuración | Texto plano | **JSON** |
| Protocolos | DHCPv4 | DHCPv4, DHCPv6, API REST |
| Alta disponibilidad | Compleja | Pares de servidores |

## Pendiente: Práctica 2
Documentar ambas instalaciones (comandos, configuración, reinicio, status) en "Desarrollo"; sin sección de Resultados. Individual, el miércoles al inicio de la clase.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! DORA
Discover (broadcast) → Offer → Request → Acknowledge (IP, máscara, gateway, DNS). PC Puma libera la IP al irse; RIU no.

| Concepto | Para recordar |
|---|---|
| 6 componentes | Ámbito, concesión, gateway, DNS, reservas, exclusiones |
| Amenazas | Starvation, Rogue DHCP; defensa: DMZ, firewall, VPN |
| ISC vs. KEA | Obsoleto 2022, monohilo, texto / multihilo, JSON, REST |
