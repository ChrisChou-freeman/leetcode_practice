class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sl = [ s for s in s.split(' ') if s != '' ]
        return len(sl[-1])

s = Solution()
assert s.lengthOfLastWord('Hello World') == 5
assert s.lengthOfLastWord('   fly me   to   the moon  ') == 4
assert s.lengthOfLastWord('luffy is still joyboy') == 6
