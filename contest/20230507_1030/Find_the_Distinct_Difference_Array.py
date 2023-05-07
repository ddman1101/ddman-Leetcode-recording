class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            prefix = nums[0:i+1]
            suffix = nums[i+1:len(nums)]
            set_prefix = set(prefix)
            set_suffix = set(suffix)
            answer.append(len(set_prefix) - len(set_suffix))
        return answer