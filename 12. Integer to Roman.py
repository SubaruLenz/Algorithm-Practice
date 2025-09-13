roman = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        index = len(roman) - 1  # Initialize index to the last valid position

        while num >= 0 and index >= 0:
            keyWord = list(roman.keys())[index]
            keyValue = roman[keyWord]
            
            if num >= keyValue:
                ans += keyWord
                num -= keyValue
            else:
                index -= 1  # Move to the next lower value
                
        return ans
