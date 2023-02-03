class Roman:
    def romanToInt(self, roman: str) -> int:
        romanNumerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        result = 0
        for a, b in zip(roman, roman[1:]):
            if romanNumerals[a] < romanNumerals[b]:
                result -= romanNumerals[a]
            else:
                result += romanNumerals[a]
        return result + romanNumerals[roman[-1]]


r = Roman()
print(r.romanToInt("XCVIII"))
