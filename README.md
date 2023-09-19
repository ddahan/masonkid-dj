# template-devcontainer-django-pg

This is a starter Template to get a Django ready-to-use Django project


### Package management

### Specifications

- Main containers: Python/Django (service_app) and PostgreSQL (service_db)
- Environment variables are handled with `.env` file (thanks to django-environ)
- Linting: Uses Ruff for linting and import sorting
- Formatting: Used Black for auto-formatting
- Package manager: Poetry
- No front-end configuration

### .env

- environment files are currently versionned becaure they are required to create the container without error.
Once the container is created, you should unversion them by adding them to `.gitignore`.

### How to run a local server

- Run `./manage.py runserver`
- Go to "http://localhost:8000/dj_admin" to ensure everything works