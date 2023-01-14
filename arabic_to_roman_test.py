from unittest import TestCase

from arabic_to_roman import ArabicRomanConverter

class TestArabicRomanConverter(TestCase):
    def test_number_one_to_I(self):
        converter = ArabicRomanConverter()
        self.assertEqual(converter.convert(1), "I")