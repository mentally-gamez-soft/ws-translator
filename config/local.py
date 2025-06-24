"""Define the local dev configuration to load for the application."""

from .default import *

# Load environment variables from local.env file
if not load_dotenv(join(BASE_DIR, "config/local.env")):
    raise Exception("Failed to load environment variables from local.env file")

APP_ENV = APP_ENV_LOCAL

if APP_USES_DATABASE:
    DB_HOSTNAME = os.environ.get("DB_HOSTNAME", "")
    DB_PORT = os.environ.get("DB_PORT", "")
    DB_USERNAME = os.environ.get("DB_USERNAME", "")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
    DB_NAME = os.environ.get("DB_NAME", "local_dev")
    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/{}.db".format(DB_NAME)
LOCAL_DEV = True
DEBUG = True
FLASK_DEBUG = True

print("--=== Local dev environment configuration loaded successfully. ===--")
