class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        while index < len(nums):
            cul_item = nums[index]
            if cul_item == val:
                del nums[index]
                index -= 1
            index += 1
        print(nums)
        return len(nums)

s = Solution()
assert s.removeElement([3,2,2,3], 3) == 2
