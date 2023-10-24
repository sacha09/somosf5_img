# somosf5_img

Prueba técnica para somos F5

## Decisiones tomadas en el desarrollo

### No branching

Como desarrollador en solitario en entorno local y sin deployment no hago branches.  

En proyecto con deployment suelo tener tres branche (main, rc/testing, development).  El trabajo a diario se hace en development, y se van haciendo merges, a rc (release candidate) donde se hacen las pruebas, y main que va a deployment.

Si el desarrollo es en equipo se hacen new function branches desde development y luego se hacen merges.

### Stack

- Web Framework: Django (Full-Stack , MVC, serverside rendering, ORM incluido, templating incluido, admin panel incluido, robusto, escalable, API friendly)
- Base de datos: sqlite (SQL en un archivo, perfecto para fast prototyping)
- Libreria CSS: picoCSS (libreria minimalista para HTML semántico)
- Libreria JS: AlpineJS (ligero, simple y poderoso, con sintaxis inspirado en vuejs)

### Permisos dentro de la app

- Los usuarion admin (superusuarios) pueden subir, modificar y eliminar fotos.
- Los usuarios registrados pueden marcar fotos como favoritas y tambien desmarcarlas.
- Los usuarios no registrados pueden ver las fotos.

## Instalación local

### Requisitos

- Python 3.10 ó superior.
- Navegador web

### Guía paso a paso

#### Crear entorno virtual

```terminal
python -m venv .venv
```

#### Iniciar entorno virtual

En windows:

```terminal
.\.venv\Scripts\activate
```

En macOS o Linux:

```terminal
source .venv/bin/activate
```

#### Instalar requisitos

```terminal
pip install -r requirements.txt
```

#### Migrar base de datos

```terminal
python manage.py migrate
```

#### Recolecta los ficheros staticos

```terminal
python manage.py collectstatic --noinput
```

#### Crear usuario administrador (superusuario)

```terminal
python manage.py createsuperuser
```

#### Activar servidor local

```terminal
python manage.py runserver
```

### Navegación de la aplicación

**Home page**

http://127.0.0.1:8000/ 

**Admin page**

http://127.0.0.1:8000/admin