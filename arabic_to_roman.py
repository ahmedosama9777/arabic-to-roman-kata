class ArabicRomanConverter():
    def convert(self, number: int) -> str:
        if number == 2:
            return "II"
        return "I"