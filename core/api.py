"""Define the api application."""

import logging
import os
from functools import wraps

from flask import Blueprint, current_app, jsonify, request
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename

from core import csrf
from core.services.translator_service import TranslatorService
from core.validators.translate_payload_validators import (
    valid_translate_payload,
)

logger = logging.getLogger(__name__)

API_TITLE: str = "{}".format(os.environ.get("APP_NAME", "Service-Name"))
API_PREFIX: str = "/{}/api/".format(API_TITLE)
API_VERSION: str = "{}".format(os.environ.get("APP_VERSION", "v0.0.1"))
ROUTE_WELCOME: str = "".join([API_PREFIX, API_VERSION])
ROUTE_TRANSLATE: str = "".join([API_PREFIX, API_VERSION, "/translate"])

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


@api_bp.route("/translate", methods=["POST"])
@api_bp.route(ROUTE_TRANSLATE, methods=["POST"])
@api_bp.route(ROUTE_TRANSLATE + "/", methods=["POST"])
def translate():
    """Translate a list of texts to the desired language."""
    logger.info(
        "Call of translate endpoint - headers {}".format(request.headers)
    )

    payload = request.get_json()
    if not payload:
        logger.error("No payload provided for translation.")
        return jsonify({"error": "No payload provided"}), 400
    if not valid_translate_payload(payload):
        logger.error("Invalid payload format. Expected a JSON object.")
        return jsonify({"error": "Invalid payload format"}), 400

    # Example translation logic (to be replaced with actual implementation)
    paragraphes = payload.get("paragraphes", [])
    target_language = payload.get("target_language", "en")

    logger.info(f"Translating {paragraphes} paragraphs to {target_language}.")

    translator_service = TranslatorService(paragraphes=paragraphes)
    response = translator_service.execute_translation(
        mode="batch",
        dest=str(target_language).strip(),
        text=None,
        texts=paragraphes,
    )
    if not response:
        logger.error("Translation failed or returned empty response.")
        return jsonify({"error": "Translation failed"}), 500

    return jsonify({"status": "ok", "translated_text": response}), 200
