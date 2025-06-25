"""This module contains validators for translation payloads."""


def valid_translate_payload(payload):
    """
    Validate the payload for translation requests.

    Args:
        payload (dict): The payload to validate.

    Returns:
        bool: True if the payload is valid, False otherwise.
    """
    required_keys = ["paragraphes", "target_language"]

    if not isinstance(payload, dict):
        return False
    for key in required_keys:
        if key not in payload:
            return False

    return True
