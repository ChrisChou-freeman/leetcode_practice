class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
       num = int(''.join([str(d) for d in digits]))
       num += 1
       return [ int(d) for d in  str(num)]

s = Solution()
assert s.plusOne([1,2,3]) == [1,2,4]
assert s.plusOne([4,3,2,1]) == [4,3,2,2]
assert s.plusOne([9]) == [1,0]
