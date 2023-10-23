# somosf5_img
Prueba técnica para somos F5

## Decisiones tomadas en el desarrollo

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

#### Crear usuario administrador

```terminal
python manage.py createsuperuser
```