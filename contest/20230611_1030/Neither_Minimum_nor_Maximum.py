class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) != 0:
            del nums[len(nums)-1]
        if len(nums) != 0:
            del nums[0]
        if len(nums) != 0:
            return nums[0]
        else:
            return -1