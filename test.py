from сonverter import NumberToWordsConverter 
import unittest

class TestNumberToWordsConverter(unittest.TestCase):
    def test_convert_to_words_single_digit(self):
        converter = NumberToWordsConverter()
        result = converter.convert_to_words(5)
        self.assertEqual(result, "five")

    def test_convert_to_words_teens(self):
        converter = NumberToWordsConverter()
        result = converter.convert_to_words(17)
        self.assertEqual(result, "seventeen")

    def test_convert_to_words_multiple_of_ten(self):
        converter = NumberToWordsConverter()
        result = converter.convert_to_words(30)
        self.assertEqual(result, "thirty")

    def test_convert_to_words_multiple_of_ten_with_units(self):
        converter = NumberToWordsConverter()
        result = converter.convert_to_words(42)
        self.assertEqual(result, "forty two")
