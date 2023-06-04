class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        position_dict = {}
        position_dict[1] = nums.index(1)
        position_dict[len(nums)] = nums.index(len(nums))
        times = 0
        while (nums.index(1) != 0) or (nums.index(len(nums)) != (len(nums) - 1)):
            if position_dict[1] != 0:
                nums[position_dict[1] - 1], nums[position_dict[1]] = nums[position_dict[1]], nums[position_dict[1] - 1]
                position_dict[1] = nums.index(1)
                position_dict[len(nums)] = nums.index(len(nums))
            elif (position_dict[1] == 0) and (position_dict[len(nums)] != (len(nums) - 1)):
                nums[position_dict[len(nums)] + 1], nums[position_dict[len(nums)]] = nums[position_dict[len(nums)]], nums[position_dict[len(nums)] + 1]
                position_dict[1] = nums.index(1)
                position_dict[len(nums)] = nums.index(len(nums))
            times += 1
        return times