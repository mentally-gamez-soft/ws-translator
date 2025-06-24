"""Define the default configuration to load for the application."""

import os
from os.path import abspath, dirname, join

from dotenv import load_dotenv

# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))

# Load environment variables from .env file
if not load_dotenv(join(BASE_DIR, "config/.env")):
    raise Exception("Failed to load environment variables from .env file")

# Application information
APP_NAME = os.environ.get("APP_NAME", "MyApp")
APP_VERSION = os.environ.get("APP_VERSION", "0.0.1")
APP_USES_DATABASE = (
    os.environ.get("APP_USES_DATABASE", "True").lower() == "true"
)
APP_SEND_EMAILS = os.environ.get("APP_SEND_EMAILS", "True").lower() == "true"

# logs files directories
LOG_PATH = join(BASE_DIR, os.environ.get("LOG_PATH", "logs"))
print("log path -> ", LOG_PATH)
LOG_FILENAME = os.environ.get("LOG_FILENAME", "app.log")

# Media dir
MEDIA_DIR = join(BASE_DIR, "media")
POSTS_IMAGES_DIR = join(MEDIA_DIR, "posts")

# Max file size for uploads
MAX_FILE_SIZE = os.environ.get("MAX_FILE_SIZE", 16)  # defaults to 16 MB

SECRET_KEY = os.environ.get("SECRET_KEY")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# App environments
APP_ENV_LOCAL = os.environ.get("APP_ENV_LOCAL")
APP_ENV_TESTING = os.environ.get("APP_ENV_TESTING")
APP_ENV_DEVELOPMENT = os.environ.get("APP_ENV_DEVELOPMENT")
APP_ENV_STAGING = os.environ.get("APP_ENV_STAGING")
APP_ENV_PRODUCTION = os.environ.get("APP_ENV_PRODUCTION")
APP_ENV = ""

# Configuración del email
if APP_SEND_EMAILS:
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT"))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    DONT_REPLY_FROM_EMAIL = tuple(
        os.environ.get("DONT_REPLY_FROM_EMAIL").split(",")
    )
    ADMINS = tuple(os.environ.get("ADMINS").split(","))
    MAIL_USE_TLS = True
    MAIL_DEBUG = False

# configure pagination
ITEMS_PER_PAGE = 20

DEBUG = False
TESTING = False
WTF_CSRF_ENABLED = True
