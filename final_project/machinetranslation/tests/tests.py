import unittest
from machinetranslation import translator

class Test_Translator(unittest.TestCase):
    def test_null_englishToFrench(self):
        self.assertEqual(translator.english_to_french(''),"Please enter text to translate")

    def test_null_FrenchToEnglish(self):
        self.assertEqual(translator.french_to_english(''),"Please enter text to translate")

    def test_FrenchForHello(self):
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')

    def test_EnglishForBonjour(self):
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')
    
unittest.main()