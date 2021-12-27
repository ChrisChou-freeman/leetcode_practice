
ROMAN_INTEGER_MAP = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
SPECIAL_RI_MAP = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}


class Solution:
    def romanToInt(self, s: str) -> int:
        v = 0
        for s_ri in SPECIAL_RI_MAP:
            if s_ri in s:
                s = s.replace(s_ri, '')
                v += SPECIAL_RI_MAP[s_ri]
        for ri in s:
            v += ROMAN_INTEGER_MAP.get(ri, 0)
        return v


s = Solution()
assert s.romanToInt('LVIII') == 58
assert s.romanToInt('MCMXCIV') == 1994
