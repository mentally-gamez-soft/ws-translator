"""Define the tests configuration to load for the application."""

from .default import *

# Load environment variables from testing.env file
if not load_dotenv(join(BASE_DIR, "config/testing.env")):
    raise Exception(
        "Failed to load environment variables from testing.env file"
    )

if APP_USES_DATABASE:
    DB_HOSTNAME = os.environ.get("DB_HOSTNAME", "")
    DB_PORT = os.environ.get("DB_PORT", "")
    DB_USERNAME = os.environ.get("DB_USERNAME", "")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
    DB_NAME = os.environ.get("DB_NAME", None)

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///instance/{}.db".format(DB_NAME)
        if DB_NAME
        else "sqlite:///:memory:"
    )

DEBUG = True
TESTING = True
APP_ENV = APP_ENV_TESTING
WTF_CSRF_ENABLED = False

print("--=== Testing environment configuration loaded successfully. ===--")
