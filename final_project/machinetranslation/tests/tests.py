import unittest
from translator import english_to_french, french_to_english

class Test_MachineTranslator(unittest.TestCase):
    def test_english_to_french(self):
        input_word = 'Hello'
        expected_output = 'Bonjour'
        translated = english_to_french(input_word)
        self.assertEqual(translated, expected_output)

    def test_french_to_english(self):
        input_word = 'Bonjour'
        expected_output = 'Hello'
        translated = french_to_english(input_word)
        self.assertEqual(translated, expected_output)