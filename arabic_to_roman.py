class ArabicRomanConverter():
    arabicDigits = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romanDigits = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]

    def convert(self, arabic: int) -> str:
        roman: str = "" 
        
        for i in range(len(self.arabicDigits) - 1, -1, -1):
            while arabic >= self.arabicDigits[i]:
                roman += self.romanDigits[i]
                arabic -= self.arabicDigits[i]
        
        return roman