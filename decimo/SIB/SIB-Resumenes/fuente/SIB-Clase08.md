% materia: Seguridad Informática Básica
% titulo: Clase 8 · Amenaza vs. vulnerabilidad: método y casos
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · jueves 24 sep 2026 · Tema 2 (2.2) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. El error más común: confundir vulnerabilidad con acción
Al regresar la actividad de la Clase 7, la profesora corrigió: la **amenaza** es "lo malo que podría pasar"; una **carencia** ya es una vulnerabilidad.
- "Falta personal" **no** es amenaza: es vulnerabilidad. Su amenaza: que alguien robe al no haber quien vigile.
- "Falta orden al manipular el material" → amenaza: que alguien resulte dañado o se pierdan cosas.
Repaso: la vulnerabilidad es la debilidad de los procedimientos ("talón de Aquiles"); se identifica preguntando **qué falta, qué no se ha hecho o qué se omitió**; puede ser humana, de hardware, de red, de software o física. Hay **riesgo** cuando una amenaza tiene una vulnerabilidad correspondiente.
!!! Las cinco reglas
1. Las amenazas **no** son vulnerabilidades.
2. Las amenazas **explotan** (aprovechan) vulnerabilidades.
3. Una amenaza puede explotar una o **varias** vulnerabilidades.
4. Una vulnerabilidad puede ser explotada por una o **varias** amenazas.
5. Las vulnerabilidades son **omisiones**: algo que falta o de lo que se carece.
"Exploits": en el ámbito profesional, programas o pruebas para identificar o aprovechar vulnerabilidades.

## 2. Reformular como "carencia de…" (activo: el celular)
**Amenazas** al celular: que se rompa, lo roben, se caiga al agua, se infle la batería y explote, se apague y no prenda, se formatee solo, se dañe la pantalla, roben las tarjetas por NFC. Que sean "malas" depende del contexto (apagarse no daña si no se iba a usar).
| Causa mal dicha | Vulnerabilidad bien dicha | Acción para reducirla |
|---|---|---|
| "Los materiales son malos" | Carece de materiales de buena calidad | Investigar marcas, pruebas de resistencia (tipo Profeco) |
| "No tenía funda" | Carece de funda de protección | Elegir funda adecuada (bordes acolchados, esquinas reforzadas) |
| "No tuve cuidado" | Carece de cuidado | Correas o amarres |
| "Se rayó" | Carece de mica protectora | Cristal templado |
| "Es bien confiado" | Carece de desconfianza | — |
| "Se enferma seguido" | Carece de buena salud | — |
Regla: si no se puede plantear como **"me falta…" / "carezco de…"**, no es vulnerabilidad.

## 3. Vulnerabilidades humanas: el eslabón más débil
Exceso de confianza, flojera, ingenuidad y falta de desconfianza:
- **Sesiones abiertas** en computadoras compartidas (las de la Facultad) o prestar el celular → falta de cuidado al cerrar sesión.
- **Modas de IA** (fotos estilo Studio Ghibli o años 80): la imagen pasa a la herramienta → falta de cuidado con la propia imagen.
- **Fotos de menores** en redes (primer día de clases, número de casa visible): facilitan ubicarlos y terminan en contextos de explotación.
- **Suplantación** con fotos robadas de perfiles públicos para dar credibilidad a perfiles falsos.
- **Prestigio irrecuperable:** lo que se sube no se retira por completo (caso de un canal familiar que ridiculizaba a sus hijos; Costa Rica regula más estrictamente).
- **Presión y miedo:** entregar contraseñas por teléfono "de parte del jefe" sin verificar.

## 4. Ejercicio de 20 reactivos (participación)
Completar con el elemento contrario. Selección:
| Dado | Se completa con |
|---|---|
| Que entren a mi Facebook (A) | No usar contraseña segura ni verificación en dos pasos (V) |
| No seguir normas de cableado estructurado (V) | Fallas de red, cortos, pérdida de conectividad (A) |
| No tener antivirus (V) | Que se infecte con malware (A) |
| Resbalarse en el pasillo (A) | Piso mojado sin señalización (V) |
| Confianza plena en un amigo (V) | Que me dé información falsa (A) |
| Perder el proyecto final (A) | No contar con respaldo (V) |
| Quedarse sin red en sesión en línea (A) | No tener respaldo de conexión (datos móviles) (V) |
| Perder la contraseña de un servicio (A) | No usar gestor de contraseñas (V) |
| Falta de pintura no inflamable (V) | Que un incendio se propague (A) |
| Omitir protecciones contra filtraciones (V) | Daño a equipos o documentos por agua (A) |
Conclusión: la vulnerabilidad se identifica preguntando **"¿qué NO se ha hecho?"**; al eliminarlas bajan los riesgos y los ataques.

## 5. Casos reales de vulnerabilidades no gestionadas
- **Línea 12 del Metro:** se descartó la ruta técnicamente más viable por razones políticas (inaugurar en la administración vigente); no se calculó bien el material de la ruta más larga y se rellenaron columnas con materiales inadecuados → fallas estructurales.
- **Recorte de seguros médicos** para ahorrar: graves consecuencias cuando alguien clave enferma o fallece.
- **Trampa en exámenes:** no prever que el alumnado use cierta tecnología (exceso de confianza en el proceso).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Definición operativa (examen)
**Vulnerabilidad = carencia u omisión** ("me falta…", "carezco de…"), nunca una acción ni el evento dañino. **Amenaza = lo malo que puede pasar**, que explota vulnerabilidades. Relación uno a muchos y muchos a muchos.

**Factor humano.** El eslabón más débil: sesiones abiertas, fotos a la IA, fotos de menores, suplantación, presión telefónica.

| Ejercicio tipo | Ejemplo |
|---|---|
| Reformular | "No tuve cuidado" → carece de cuidado |
| Completar A → V | Perder el proyecto → no tener respaldo |
| Completar V → A | Sin antivirus → infección por malware |
| Caso real | Línea 12: omisiones de planeación → colapso |
