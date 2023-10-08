# Django Mason Kid Starter

A minimal Django Starter Template for quick SaaS.


### Specifications

- Main containers: Python/Django (service_app) and PostgreSQL (service_db)
- Environment variables are handled with `.env` file (via django-environ)
- Linting / Imports auto-sorting: Ruff
- Auto-Formatting: Black
- Package management: Poetry
- No front-end configuration

## How To

#### Before cloning the container:
- Open Docker Desktop and ddd `/workspaces` directory in settings > Resources > File sharing.
- Install [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) in VS Code
- Run `Clone Repository` command and clone this repository.


#### Once the container has been created:
- Reload the container once (running the `reload window` VS Code command ) to ensure there is no error with extension activation due to a Dev Container bug.
- Create a `.env` file based on `.env.example` file.
- Run `./manage.py migrate`
- Run `./manage.py runserver` and go to "http://localhost:8000/" to ensure everything works.
