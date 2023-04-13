"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res   = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                stack_num, stack_int = stack.pop()
                res[stack_int] = i - stack_int
            stack.append((t, i))
        return res