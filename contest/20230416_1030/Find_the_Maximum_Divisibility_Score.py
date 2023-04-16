class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        scores = []
        for i in range(len(divisors)):
            new_nums = [x for x in nums if x % divisors[i] == 0]
            scores.append(len(new_nums))
        # judge the minimum number for the maximum scores
        max_pos = []
        for j in range(len(scores)):
            if max(scores) == scores[j]:
                max_pos.append(j)
        min_num = max(divisors)
        for k in range(len(max_pos)):
            if min_num > divisors[max_pos[k]] :
                min_num = divisors[max_pos[k]]
        return min_num