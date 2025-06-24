#!/bin/bash
. $HOME/.profile;

# Ask the user for the environment
read -p "Please indicate on which environment you want to work on ? [dev, staging, prod]: " ENVIRONMENT

ENVIRONMENT=$(echo "$ENVIRONMENT" | tr '[:upper:]' '[:lower:]');

if [[ "$ENVIRONMENT" != "dev" && "$ENVIRONMENT" != "staging" && "$ENVIRONMENT" != "prod" ]]; then
    echo "Error - The chosen environment is invalid !";
    exit 10;
fi;

echo "You chose to work on ${ENVIRONMENT} environment.";

# Show the current name of the application:
CURRENT_APP_NAME=`head -1 Docker/application/${ENVIRONMENT}/app.name.env | cut -d'=' -f2`;
echo "The application name is currently ${CURRENT_APP_NAME} for the environment ${ENVIRONMENT}";

# Ask the user to give a name to the application
read -p "Please indicate the name of this application: " APPLICATION_NAME

if [[ "$APPLICATION_NAME" == "" ]]; then
    APPLICATION_NAME="${CURRENT_APP_NAME}";
fi;

echo "The application is now named: ${APPLICATION_NAME}.";
echo "APP_NAME=${APPLICATION_NAME}" > Docker/application/${ENVIRONMENT}/app.name.env; 
echo 'apres ecriture ficher => $?';

# Show the current version of the image:
CURRENT_VERSION_NUMBER=`head -1 Docker/application/${ENVIRONMENT}/app.version.env`;
echo "The application is currently base on image version number ${CURRENT_VERSION_NUMBER} for the environment ${ENVIRONMENT}";

# Ask the user for the version of the app
read -p "Please indicate the new version of the application (eg: 0.3.1f) for the environment ${ENVIRONMENT} " VERSION_NUMBER

VERSION_PATTERN="^[0-9]\.[0-9]\.[0-9][a-zA-Z]$"

# check the version number with the pattern
if ! [[ "$VERSION_NUMBER" =~ $VERSION_PATTERN ]]; then
echo "Error - The input version number is invalid!";
    exit 20;
fi; 

echo "APP_VERSION=\"${VERSION_NUMBER}\"" > Docker/application/${ENVIRONMENT}/app.version.env;

echo "The application version number env file has been updated (Docker/application/${ENVIRONMENT}/app.version.env).";

export APP_VERSION="$VERSION_NUMBER";
export APP_ENV="$ENVIRONMENT";
export APP_NAME="$APPLICATION_NAME";
export DOCKERREGISTRY="$DOCKER_REGISTRY";
export DOCKERREPOSITORY="$DOCKER_REPOSITORY";

echo "The env variable APP_VERSION has been updated -> ${APP_VERSION}";
echo "The env variable APP_ENV has been updated -> ${APP_ENV}";
echo "docker repo -> ${DOCKERREPOSITORY}";
echo "docker reg -> ${DOCKERREGISTRY}";

docker compose -f Docker/application/${ENVIRONMENT}/docker-compose-${ENVIRONMENT}.yaml build --build-arg DOCKERREPOSITORY=${DOCKERREPOSITORY}