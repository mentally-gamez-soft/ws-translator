"""TranslatorService: A service for translating text using Google Translate API."""

import asyncio
import logging

from googletrans import Translator

logger = logging.getLogger(__name__)


class TranslatorService:
    """Service to handle translation operations."""

    def __init__(self, paragraphes: list[str] = None):
        """Initialize the TranslatorService with an optional list of paragraphs."""
        self.translator = Translator()
        self.paragraphes = paragraphes

    def add_paragraphe(self, paragraphe: str):
        """Add a paragraph to the list of paragraphs to translate."""
        if self.paragraphes is None:
            self.paragraphes = []
        self.paragraphes.append(paragraphe)

    async def translate(self, dest: str = "en", text: str = None) -> str:
        """Translate a single text to the specified language.

        Args:
            dest (str, optional): The destination language for the translation. Defaults to english.
            text (str, optional): The text to translate. Defaults to None.

        Returns:
            str: The translated text.
        Raises:
            ValueError: If no text is provided for translation.
        """
        if not text:
            raise ValueError("No text provided for translation.")
        result = await self.translator.translate(dest, text)
        return result.text

    async def batch_translate(
        self, dest: str = "en", texts: list[str] = None
    ) -> list[str]:
        """Translate a batch of texts to the specified language.

        Args:
            dest (str, optional): The destination language for the translation. Defaults to english.
            texts (list[str], optional): A list of texts to translate. Defaults to None.

        Returns:
            list[str]: A list of translated texts.
        Raises:
            ValueError: If no texts or paragraphs are provided for translation.
        """
        if texts:
            tasks = [self.translate(text, dest) for text in texts]
        else:
            if not self.paragraphes:
                raise ValueError("No paragraphs to translate.")
            tasks = [self.translate(dest, text) for text in self.paragraphes]
        return await asyncio.gather(*tasks)

    def execute_translation(
        self,
        mode: str = "single",
        dest: str = "en",
        text: str = None,
        texts: list[str] = None,
    ) -> list[str]:
        """Execute translation based on the specified mode.

        Args:
            mode (str, optional): The mode to execute single or batch. Defaults to "single".
            dest (str, optional): The destination language for the translation. Defaults to english.
            text (str, optional): The text to translate. Defaults to None.
            texts (list[str], optional): A list of texts to translate. Defaults to None.

        Raises:
            ValueError: If an invalid mode is provided.

        Returns:
            list[str]: The translated text or list of translated texts based on the mode.
        """
        logger.info(
            f"Executing translation in {mode} mode to {dest} with text: {text} and texts: {texts}"
        )
        if mode == "single":
            return [
                asyncio.run(self.translate(dest, text)),
            ]
        elif mode == "batch":
            return asyncio.run(self.batch_translate(dest=dest, texts=texts))
        else:
            raise ValueError("Invalid mode. Use 'single' or 'batch'.")
