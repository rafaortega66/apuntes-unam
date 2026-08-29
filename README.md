# Apuntes — sitio estático

Sitio de apuntes del semestre, listo para hostear gratis en **GitHub Pages**.
Todo son archivos reales (HTML + PDFs); nada corre en un sandbox, así que
los PDFs se abren nativos en el navegador.

## Estructura

```
index.html                          ← página de inicio (lista de materias)
assets/style.css                    ← estilos compartidos
materias/
  arquitectura-cliente-servidor/
    index.html                      ← info de la materia + ligas + secciones
    evaluacion.html                 ← criterios de evaluación, tarea #1, etc.
    tema-01.html                    ← apuntes del tema + botones a los PDFs
    files/
      Tema-01-Procesos-diapositivas.pdf
      Tema-01-Procesos-manual.pdf
  reconocimiento-de-patrones/
    index.html                      ← placeholder, se llena después
  ...(resto de las 9 materias)
```

## Cómo llevarlo a producción con Claude Code

1. Abre esta carpeta en **Claude Code** (o cópiala a un repo local).
2. Inicializa el repo y súbelo a GitHub:
   ```bash
   git init
   git add .
   git commit -m "Sitio inicial de apuntes"
   gh repo create apuntes-unam --public --source=. --push
   ```
   (si no tienes `gh` instalado, crea el repo manualmente en github.com y usa
   `git remote add origin <url>` + `git push -u origin main`)
3. Activa GitHub Pages: en el repo → **Settings → Pages → Branch: main → /(root)**.
4. En un par de minutos tu sitio queda disponible en:
   `https://<tu-usuario>.github.io/apuntes-unam/`

## Cómo seguir agregando contenido

Cada vez que quieras agregar apuntes de una clase nueva o una materia nueva,
pídele a Claude Code que:
- cree/edite el `index.html` de la materia correspondiente, o
- agregue una página nueva (como `tema-02.html`) siguiendo el mismo patrón
  de `tema-01.html`, y
- copie cualquier PDF nuevo dentro de la carpeta `files/` de esa materia.

Luego solo es `git add . && git commit -m "..." && git push` y GitHub Pages
se actualiza solo.
