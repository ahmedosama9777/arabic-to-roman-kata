class ArabicRomanConverter():
    def convert(self, arabic: int) -> str:
        roman: str = ""

        for i in range(arabic):
            roman += "I"
        
        return roman