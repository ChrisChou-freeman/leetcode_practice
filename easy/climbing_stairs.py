from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n-2) + self.climbStairs(n-1)

s = Solution()
print(s.climbStairs(3))
