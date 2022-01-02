class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        max_val = nums[0]
        sum_val = nums[0]
        for i in range(1, len(nums)):
            sum_val = max(nums[i], sum_val + nums[i])
            max_val = max(sum_val, max_val)
        return max_val

s = Solution()
assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert s.maxSubArray([1]) == 1
assert s.maxSubArray([-1]) == -1
assert s.maxSubArray([5,4,-1,7,8]) == 23
assert s.maxSubArray([-2, -1]) == -1
