"""Define the production configuration to load for the application."""

from .default import *

# Load environment variables from prod.env file
if not load_dotenv(join(BASE_DIR, "config/prod.env")):
    raise Exception("Failed to load environment variables from prod.env file")

if APP_USES_DATABASE:
    DB_HOSTNAME = os.environ.get("DB_HOSTNAME", "serverdb")
    DB_PORT = os.environ.get("DB_PORT", "5432")
    DB_NAME = os.environ.get("DB_NAME", "prod_db")
    DB_USERNAME = os.environ.get("DB_USERNAME", "postgres")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "test_123")

    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
        DB_USERNAME, DB_PASSWORD, DB_HOSTNAME, DB_PORT, DB_NAME
    )

APP_ENV = APP_ENV_PRODUCTION

print("--=== Prod environment configuration loaded successfully. ===--")
