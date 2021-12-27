class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        if sx.startswith('-'):
            return False
        sxl = list(sx)
        sxl.reverse()
        sx2 = ''.join(sxl)
        if sx != sx2:
            return False
        return True

s = Solution()
assert s.isPalindrome(121)
