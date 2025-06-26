import json

from tests import BaseTestClass


class TestTranslateApi(BaseTestClass):
    def test_translate_api(self):
        payload = {}
        payload["paragraphes"] = [
            "Hola mundo.",
            "Yo no voy a ir.",
            "Estoy cansado.",
            "Muchas gracias amigo.",
        ]
        payload["target_language"] = "fr"
        response = self.app.test_client().post("/translate", json=payload)
        response_message = json.loads(response.text)
        self.assertEqual(
            200,
            response.status_code,
            " The response status code should be 200 - {}.".format(
                response.text
            ),
        )
        self.assertTrue(response_message["status"], "ok")
        self.assertEqual(
            len(response_message["translated_text"]),
            len(payload["paragraphes"]),
        )
        self.assertEqual(
            response_message["translated_text"][0], "Bonjour le monde."
        )
        self.assertEqual(
            response_message["translated_text"][1], "Je ne vais pas y aller."
        )
        self.assertEqual(
            response_message["translated_text"][2], "Je suis fatigué."
        )
        self.assertEqual(
            response_message["translated_text"][3], "Merci beaucoup mon pote."
        )
