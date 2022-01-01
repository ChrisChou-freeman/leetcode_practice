class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) < 2:
            if target > nums[0]:
                return 1
            else:
                return 0
        index = 1
        while True:
            pre_item = nums[index-1]
            cur_item = nums[index]
            if target < pre_item:
                return index - 1
            elif target > pre_item and target < cur_item:
                return index
            elif target == pre_item:
                return index - 1
            elif target == cur_item:
                return index
            index += 1
            if index >= len(nums):
                return index

s =  Solution()
assert s.searchInsert([1,3,5,6], 5) == 2
assert s.searchInsert([1,3,5,6], 2) == 1
assert s.searchInsert([1,3,5,6], 7) == 4
