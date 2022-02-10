import unittest
from translator import french_to_english, english_to_french

class testTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('I am a test'), 'Je suis un test')
        self.assertEqual(english_to_french(''), '')


    def test_french_to_english(self):
        self.assertEqual(french_to_english('Je suis un test'), 'I am a test')
        self.assertEqual(french_to_english(''), '')


unittest.main()