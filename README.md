# ws-translator
web service to translate text

## Set the environment variables

    export FLASK_APP="application"
    export FLASK_ENV="development"
    export APP_SETTINGS_MODULE="config.local"

## Testing application
### Run the application

    uv run -m unittest tests.test_index

## Run the application locally

    uv run -m flask --app application run --port 3456 --host 0.0.0.0