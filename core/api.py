"""Define the api application."""

import logging
import os
from functools import wraps

from flask import Blueprint, current_app, jsonify, request
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename

from core import csrf

logger = logging.getLogger(__name__)

API_TITLE: str = "{}".format(os.environ.get("APP_NAME", "Service-Name"))
API_PREFIX: str = "/{}/api/".format(API_TITLE)
API_VERSION: str = "{}".format(os.environ.get("APP_VERSION", "v0.0.1"))
ROUTE_WELCOME: str = "".join([API_PREFIX, API_VERSION])

api_bp = Blueprint("api_urls", __name__)


@api_bp.route(ROUTE_WELCOME, methods=["GET"])
@api_bp.route(ROUTE_WELCOME + "/", methods=["GET"])
@api_bp.route("/", methods=["GET"])
def default():
    """Define a test endpoint to check the webservice status."""
    logger.info(
        "Call of welcome endpoint - headers {}".format(request.headers)
    )

    return (
        jsonify(
            "Welcome to {} service. (You're using the version {})".format(
                API_TITLE, API_VERSION
            )
        ),
        200,
        {
            "X-CSRFToken": generate_csrf(
                secret_key=current_app.config.get("SECRET_KEY")
            )
        },
    )
