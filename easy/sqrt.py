class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0): return 0
        if (x == 1): return 1

        low, high = 0, x
        while low < high:
            mid = low + (high-low)//2
            if mid**2 <= x:
                low = mid + 1
            else:
                high = mid

        return low - 1

s = Solution()
assert s.mySqrt(8) == 2
assert s.mySqrt(4) == 2

