"""Declare the entry point for the flask application."""

import os

from core import create_app

settings_module = os.getenv("APP_SETTINGS_MODULE")
print("settings_module = {}".format(settings_module))
app = create_app(settings_module)
