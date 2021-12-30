class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 1
        while index < len(nums):
            pre_item = nums[index-1]
            cur_item = nums[index]
            if cur_item == pre_item:
                del nums[index]
                index -=1
            index += 1
        return len(nums)


s = Solution()
assert s.removeDuplicates([1,1,2]) == 2
assert s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
