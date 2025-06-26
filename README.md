# ws-translator
A web service to translate a set of texts based on Googletranslate API.

The web service is ready for executing in the following environment:
- local development
- containerized docker host development
- containerized docker host production ready (gunicorn and nginx)

A set of tools is provided to help you to create, run and stop the docker container.

## Requirements
- Python 3.11 or higher
- pip 24.0 or higher
- virtualenv 20.16.7 or higher
- uv 0.4.0 or higher
- docker 20.10.21 or higher
- docker-compose 1.29.2 or higher

## Stack Technologies
![Alt text](technology_stack.svg)

## API Endpoints
### Sanity check
    The check is located at home "/"

### Translations
    The transations endpoint is located at "/translate"

### Swagger documentations
    The swagger UI is located at "/swagger"

## Set the environment variables

    On unix OS:
     - export FLASK_APP="application"
     - export FLASK_ENV="development"
     - export APP_SETTINGS_MODULE="config.local"

    On Windows OS powershell:
     - $env:FLASK_APP="application"
     - $env:FLASK_ENV="development"
     - $env:APP_SETTINGS_MODULE="config.local"

## Running application
## Local development

    uv run -m flask --app application run --port 3456 --host 0.0.0.0

### Executing the tests suit
    uv run -m unittest tests.test_sanity_check_api
    uv run -m unittest tests.test_translate_api
    uv run -m unittest tests.services.test_translator_service

## Docker Images
### Create an image
    On unix OS:
    execute the shell ./docker_manager.sh choose option (1) and follow the instructions.

### Run a container
    On unix OS:
    execute the shell ./docker_manager.sh choose option (2) and follow the instructions.

### Stop a container
    On unix OS:
    execute the shell ./docker_manager.sh choose option (3) and follow the instructions.