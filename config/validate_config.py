"""Define the validate_env_config function."""

from flask import Config


def validate_env_config(app_config: Config):
    """Validate the environment configuration."""
    required_vars = [
        "APP_NAME",
        "APP_VERSION",
        "APP_ENV",
        "SECRET_KEY",
        "MEDIA_DIR",
        "POSTS_IMAGES_DIR",
        "MAX_FILE_SIZE",
        "APP_ENV_LOCAL",
        "APP_ENV_TESTING",
        "APP_ENV_DEVELOPMENT",
        "APP_ENV_STAGING",
        "APP_ENV_PRODUCTION",
        "APP_ENV",
        "LOG_PATH",
        "LOG_FILENAME",
    ]

    if app_config.get("APP_USES_DATABASE", False):
        required_vars.extend(
            [
                "DB_HOSTNAME",
                "DB_PORT",
                "DB_NAME",
                "DB_USERNAME",
                "DB_PASSWORD",
            ]
        )
    else:
        print(
            "No database will be used for application, skipping database configuration validation."
        )

    if app_config.get("APP_SEND_EMAILS", False):
        required_vars.extend(
            [
                "MAIL_SERVER",
                "MAIL_PORT",
                "MAIL_USERNAME",
                "MAIL_PASSWORD",
                "DONT_REPLY_FROM_EMAIL",
                "ADMINS",
            ]
        )
    else:
        print(
            "No emails will be used for application, skipping mail server configuration validation."
        )

    missing_vars = [var for var in required_vars if not app_config.get(var)]

    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )

    print("Environment configuration is valid.")
