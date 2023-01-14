from unittest import TestCase

from arabic_to_roman import ArabicRomanConverter

class TestArabicRomanConverter(TestCase):
    def setUp(self) -> None:
        self.converter = ArabicRomanConverter()

    def test_number_one(self):
        self.assertEqual(self.converter.convert(1), "I")
    
    def test_number_two(self):
        self.assertEqual(self.converter.convert(2), "II")
    
    def test_number_three(self):
        self.assertEqual(self.converter.convert(3), "III")
    
    def test_number_four(self):
        self.assertEqual(self.converter.convert(4), "IV")
    
    def test_number_five(self):
        self.assertEqual(self.converter.convert(5), "V")
    
    def test_number_seven(self):
        self.assertEqual(self.converter.convert(7), "VII")
    
    def test_number_nine(self):
        self.assertEqual(self.converter.convert(9), "IX")
    
    def test_number_ten(self):
        self.assertEqual(self.converter.convert(10), "X")
    
    def test_number_fifteen(self):
        self.assertEqual(self.converter.convert(16), "XVI")
    
    def test_number_twentyone(self):
        self.assertEqual(self.converter.convert(21), "XXI")

    def test_number_fiftyone(self):
        self.assertEqual(self.converter.convert(51), "LI")
    
    def test_number_fourthousand_nine_hundred_ninety_nine(self):
        self.assertEqual(self.converter.convert(4999), "MMMMCMXCIX")
    
    
    