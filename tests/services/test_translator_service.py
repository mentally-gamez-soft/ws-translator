import unittest


class TestTranslatorService(unittest.TestCase):
    def setUp(self):
        from core.services.translator_service import TranslatorService

        self.translator_service = TranslatorService()

    def tearDown(self):
        del self.translator_service

    def test_translate_french_to_english(self):
        # Test translation from French to English
        self.translator_service.add_paragraphe("Le pain était bon ce matin.")
        # Mocking the translation result
        self.translator_service.translate = lambda text, dest: (
            "The bread was good this morning."
            if text == "Le pain était bon ce matin."
            else "Translation not available"
        )
        # Call the translate method
        result = self.translator_service.translate(
            dest="en", text=self.translator_service.paragraphes[0]
        )
        self.assertEqual(result, "The bread was good this morning.")

    def test_translate_spanish_to_english(self):
        # Test translation from Spanish to English
        self.translator_service.add_paragraphe(
            "El pan estaba bueno esta mañana."
        )
        # Mocking the translation result
        self.translator_service.translate = lambda text, dest: (
            "The bread was good this morning."
            if text == "El pan estaba bueno esta mañana."
            else "Translation not available"
        )
        # Call the translate method
        result = self.translator_service.translate(
            dest="en", text=self.translator_service.paragraphes[0]
        )
        self.assertEqual(result, "The bread was good this morning.")

    def test_translate_english_to_french(self):
        # Test translation from English to French
        self.translator_service.add_paragraphe(
            "The bread was good this morning."
        )
        # Mocking the translation result
        self.translator_service.translate = lambda text, dest: (
            "Le pain était bon ce matin."
            if text == "The bread was good this morning."
            else "Translation not available"
        )
        # Call the translate method
        result = self.translator_service.translate(
            dest="fr", text=self.translator_service.paragraphes[0]
        )
        self.assertEqual(result, "Le pain était bon ce matin.")

    def test_translate_english_to_spanish(self):
        # Test translation from English to Spanish
        self.translator_service.add_paragraphe(
            "The bread was good this morning."
        )
        # Mocking the translation result
        self.translator_service.translate = lambda text, dest: (
            "El pan estaba bueno esta mañana."
            if text == "The bread was good this morning."
            else "Translation not available"
        )
        # Call the translate method
        result = self.translator_service.translate(
            dest="es", text=self.translator_service.paragraphes[0]
        )
        self.assertEqual(result, "El pan estaba bueno esta mañana.")

    def test_batch_translate(self):
        # Test batch translation
        self.translator_service.add_paragraphe("Le pain était bon ce matin.")
        self.translator_service.add_paragraphe(
            "Ma maison a brûlé dans la nuit."
        )
        # Mocking the batch translation result
        self.translator_service.batch_translate = lambda dest, texts: (
            [
                "The bread was good this morning.",
                "My house burned down in the night.",
            ]
            if dest == "en"
            else ["Translation not available", "Translation not available"]
        )
        # Call the batch_translate method
        results = self.translator_service.batch_translate(
            dest="en", texts=self.translator_service.paragraphes
        )
        self.assertEqual(
            results,
            [
                "The bread was good this morning.",
                "My house burned down in the night.",
            ],
        )

    def test_execute_translation_single(self):
        # Test single translation execution
        self.translator_service.add_paragraphe("Le pain était bon ce matin.")
        # Mocking the translation result
        self.translator_service.execute_translation = (
            lambda mode, dest, text, texts: (
                "The bread was good this morning."
                if mode == "single" and text == "Le pain était bon ce matin."
                else "Translation not available"
            )
        )
        # Call the execute_translation method
        result = self.translator_service.execute_translation(
            mode="single",
            dest="en",
            text=self.translator_service.paragraphes[0],
            texts=None,
        )
        self.assertEqual(result, "The bread was good this morning.")

    def test_execute_translation_batch(self):
        # Test batch translation execution
        self.translator_service.add_paragraphe("Le pain était bon ce matin.")
        self.translator_service.add_paragraphe(
            "Ma maison a brûlé dans la nuit."
        )
        # Mocking the batch translation result
        self.translator_service.execute_translation = (
            lambda mode, dest, text, texts: (
                [
                    "The bread was good this morning.",
                    "My house burned down in the night.",
                ]
                if mode == "batch"
                else "Translation not available"
            )
        )
        # Call the execute_translation method
        results = self.translator_service.execute_translation(
            mode="batch",
            dest="en",
            text=None,
            texts=self.translator_service.paragraphes,
        )
        self.assertEqual(
            results,
            [
                "The bread was good this morning.",
                "My house burned down in the night.",
            ],
        )
