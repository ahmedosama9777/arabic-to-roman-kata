class ArabicRomanConverter():
    def convert(self, arabic: int) -> str:
        roman: str = "" 

        while arabic >= 5:
            roman += "V"
            arabic -= 5

        for i in range(arabic):
            roman += "I"
        
        return roman