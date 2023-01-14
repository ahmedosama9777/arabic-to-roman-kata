from unittest import TestCase

from arabic_to_roman import ArabicRomanConverter

class TestArabicRomanConverter(TestCase):
    def test_number_one(self):
        converter = ArabicRomanConverter()
        self.assertEqual(converter.convert(1), "I")
    
    def test_number_two(self):
        converter = ArabicRomanConverter()
        self.assertEqual(converter.convert(2), "II")