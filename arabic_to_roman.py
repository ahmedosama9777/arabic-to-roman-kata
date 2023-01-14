class ArabicRomanConverter():
    def convert(self, arabic: int) -> str:
        roman: str = "" 

        if arabic == 10:
            return "X"

        while arabic >= 5:
            roman += "V"
            arabic -= 5

        for i in range(arabic):
            roman += "I"
        
        return roman