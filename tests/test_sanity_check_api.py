from core.api import ROUTE_WELCOME

from . import BaseTestClass


class WelcomeClientTestCase(BaseTestClass):

    def test_index(self):
        response = self.app.test_client().get("/")
        self.assertEqual(
            200,
            response.status_code,
            " The response status code should be 200 - {}.".format(
                response.text
            ),
        )
        self.assertIn(
            b"Welcome",
            response.data,
            "The response should contain 'Welcome' - {}.".format(
                response.data
            ),
        )
        self.assertIsNotNone(
            response.headers.get("X-CSRFToken"),
            "The response should contain 'X-CSRFToken' header - {}.".format(
                response.headers.get("X-CSRFToken")
            ),
        )
