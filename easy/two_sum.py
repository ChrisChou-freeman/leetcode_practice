class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) < 2:
            return []
        for n1 in range(len(nums)):
            for n2 in range(n1+1, len(nums)):
                if nums[n1] + nums[n2] == target:
                    return [n1, n2]
        return []

s = Solution()

assert s.twoSum([2,7,11,15], 9) == [0, 1]
assert s.twoSum([3,2,4], 6) == [1, 2]
