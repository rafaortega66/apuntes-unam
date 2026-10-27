% materia: Administración de Servicios de Internet
% titulo: Clase 14 · Seguridad y auditoría en Oracle
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · lunes 19 oct 2026 · Servidor de bases de datos · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Todo fue demostración en vivo con sqlplus y SQL Developer. Es la base de la práctica de auditoría (equipos de 3).

## 1. Usuarios, roles y privilegios
!!! Orden correcto
**Usuario → rol → privilegios.** Los privilegios se agrupan en un rol y el rol se asigna al usuario, en vez de dar permisos sueltos a cada cuenta (como un gafete de "Becario" con sus accesos ya programados).

Como administrador (SYSTEM) en sqlplus:
```
ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE;   -- evita ORA-65096 en Oracle Enterprise
CREATE USER Rafa IDENTIFIED BY 123;
CREATE ROLE becario;
GRANT CREATE SESSION TO becario;
GRANT CREATE TABLE TO becario;
GRANT INSERT ANY TABLE TO becario;
GRANT SELECT ANY TABLE TO becario;
GRANT CREATE TRIGGER TO becario;
GRANT becario TO Rafa;
```
Sin `_ORACLE_SCRIPT` sale **ORA-65096: invalid common user or role name**.

## 2. UNLIMITED TABLESPACE
El table space son los archivos donde Oracle guarda físicamente los datos. Rafa pudo crear la tabla, pero el primer `INSERT` falló:
```
CREATE TABLE reprobaditos (id NUMBER(3), fecha_completa TIMESTAMP,
                           fecha_corta DATE, nombre VARCHAR2(20));
INSERT INTO reprobaditos VALUES (1, SYSDATE, SYSDATE, 'Axel');
-- ORA-01950: no privileges on tablespace 'USERS'
```
!!! Privilegio que no va en rol
"Hay privilegios, y más cuando son de sistema operativo, que les debes asignar **directamente al usuario**." Lo que toca el almacenamiento físico no se hereda por rol: `GRANT UNLIMITED TABLESPACE TO Rafa;`
En producción, quedarse sin cuota detiene las aplicaciones conectadas.

## 3. DATE frente a TIMESTAMP
Con `SYSDATE` en ambas columnas, la consola mostró DATE como `19-OCT-26` y TIMESTAMP con hora, minuto, segundo y fracciones.
- ¿Para qué tanta precisión? Si los datos cambian dentro del mismo segundo hay que poder rastrear el orden: por eso la auditoría usa **TIMESTAMP**.
- `SYSDATE` se basa en la zona horaria local (México tiene tres zonas); no se recomienda centralizarla.
- Nota de la documentación de Oracle: DATE también guarda hora:min:seg; lo que cambia es el formato por defecto. TIMESTAMP agrega **fracciones de segundo** (6 dígitos por defecto).

## 4. Esquemas, usuario.tabla y COMMIT
Cada usuario tiene su propio esquema (una "carpeta"). Desde la cuenta Emilio:
| Consulta | Resultado | Por qué |
|---|---|---|
| `SELECT * FROM reprobaditos;` | ORA-00942: table or view does not exist | La tabla es de Rafa |
| `SELECT * FROM Rafa.reprobaditos;` | No hay filas | Rafa no ha hecho `COMMIT` |
!!! DML vs. DDL
**DML** (`INSERT`, `UPDATE`, `DELETE`) queda en una transacción privada hasta el **`COMMIT;`** ("si no está publicado, no lo puedo ver"). **DDL** (`CREATE`, `DROP TABLE`) tiene efecto inmediato, sin COMMIT.

## 5. Auditoría con disparadores
| Procedimiento almacenado | Disparador (trigger) |
|---|---|
| Lo tienes que llamar tú | **Automático**, antes o después de `INSERT`, `UPDATE` o `DELETE` |
Se usa para auditar **quién, cómo y cuándo**.
```
CREATE TABLE auditoria (usuario VARCHAR2(30), movimiento VARCHAR2(30), fecha TIMESTAMP);

CREATE OR REPLACE TRIGGER i_condicion
AFTER INSERT ON Rafa.condicion
FOR EACH ROW
BEGIN
  INSERT INTO auditoria VALUES (USER, 'inserto', SYSDATE);
END;
/
```
- `USER` devuelve la cuenta conectada que provocó el evento; `FOR EACH ROW` da una entrada por fila.
- Para la práctica, cubrir también UPDATE y DELETE con `INSERTING`, `UPDATING`, `DELETING` y las variables de fila:
- - **`:NEW.campo`**: el valor que entra (INSERT y UPDATE).
- - **`:OLD.campo`**: el valor que había antes (UPDATE y DELETE).
- La tabla de auditoría debe guardar el valor anterior y el nuevo.
Errores comunes: escribir `SHOW USER` en vez de `USER`; olvidar `FOR EACH ROW`.

## 6. SQL Developer local contra Oracle en la nube
1. En Free SQL / Live SQL, abrir la configuración de conexión y copiar host, **puerto 1521** (2484 si es cifrada), nombre de servicio y usuario; regenerar la contraseña.
2. En SQL Developer: Nueva conexión, host y puerto, tipo **Nombre de servicio (no SID)**, usuario y contraseña.
3. Probar y Conectar. Un `CREATE TABLE pruebita (id NUMBER);` local apareció en la consola web.

## 7. Práctica de auditoría (equipos de 3)
Introducción (servidor de BD y auditoría) → Desarrollo (usuarios, roles, permisos, tablas, inserciones, conexión a la nube) → Resultados (disparador con UPDATE y DELETE usando :OLD y :NEW; tabla de auditoría ampliada). Fecha: revisar Classroom.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Error / concepto | Para recordar |
|---|---|
| Orden de permisos | Usuario → rol → privilegios |
| ORA-65096 | `ALTER SESSION SET "_ORACLE_SCRIPT" = TRUE;` antes de `CREATE USER` |
| ORA-01950 | Falta `UNLIMITED TABLESPACE`: va **directo al usuario**, no por rol |
| ORA-00942 | Tabla de otro: usar `usuario.tabla` |
| Tabla vacía de otro | El dueño no hizo `COMMIT` (DML); DDL no lo necesita |
| DATE vs. TIMESTAMP | TIMESTAMP agrega fracciones de segundo: el que se usa para auditar |

!!! Disparador de auditoría (práctica)
Automático, antes/después de INSERT/UPDATE/DELETE, `FOR EACH ROW`. Guarda `USER`, el movimiento y el TIMESTAMP; con `:OLD` (antes) y `:NEW` (después) registra el valor anterior y el nuevo.

**Nube.** SQL Developer: host, puerto 1521, **nombre de servicio** (no SID), usuario y contraseña.
