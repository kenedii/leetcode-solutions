# Beats 80.53 % Runtime
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        s= s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        total = 0
        for char in s:
            total += romans[char]
        return total
