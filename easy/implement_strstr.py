class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        index_of = haystack.index(needle)
        return index_of

s = Solution()

assert s.strStr('hello', 'll') == 2
assert s.strStr('aaaaa', 'bba') == -1
assert s.strStr('', '') == 0
