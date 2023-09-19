# template-devcontainer-django-pg

This is a starter template to get ready-to-use Django/PostgreSQL project in a Dev Container.


### Specifications

- Main containers: Python/Django (service_app) and PostgreSQL (service_db)
- Environment variables are handled with `.env` file (via django-environ)
- Linting / Imports auto-sorting: Ruff
- Auto-Formatting: Black
- Package management: Poetry
- No front-end configuration

### About .env file

- .env file is currently versionned becaure it's required to create the container without error. Once the container is created, you should unversion it by adding it to `.gitignore` file.

## How To

#### Before cloning the container:
- Add `/workspaces` directory to Docker Desktop (in settings > Resources > File sharing)
- Install [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) in VS Code
- Run `Clone Repository` command and clone this repository.


#### Once the container has been created:
- If you have any VS Code error similar to "xxx extension can't be activated", just run `reload window` VS Code command.
- Run `./manage.py migrate`
- Run `./manage.py runserver` and go to "http://localhost:8000/dj_admin" to ensure everything works.
