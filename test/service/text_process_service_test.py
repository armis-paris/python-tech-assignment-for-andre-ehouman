import unittest

from src.service.text_process_service import TextProcessService


class TextProcessServiceTest(unittest.TestCase):

    def test_should_extract_information(self):
        # given
        text = 'I started to listen Nirvana band in 2009!'

        text_process_service = TextProcessService()

        # when
        text_information = text_process_service.extract_information(text)

        # then
        self.assertIsNotNone(text_information)
        assert text_information["unique_numerical_characters"] == ["2", "0", "0", "9"]

        # unique_numerical_characters_text
        unique_numerical_characters_text = '200'
        text_information = text_process_service.extract_information(unique_numerical_characters_text)
        assert text_information["unique_alphabetic_characters"] == []

        # unique_alphabetic_characters
        unique_alphabetic_characters = 'car'
        text_information = text_process_service.extract_information(unique_alphabetic_characters)
        assert text_information["unique_numerical_characters"] == []

        # unique_other_characters
        unique_other_characters = '!?%'
        text_information = text_process_service.extract_information(unique_other_characters)
        assert text_information["unique_alphabetic_characters"] == []
        assert text_information["unique_numerical_characters"] == []
        assert text_information["unique_other_characters"] == ["!", "?", "%"]
