class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        total_stack = [0,0]
        for i in range(len(mat)):
            if sum(mat[i]) != 0:
                if total_stack[1] < sum(mat[i]):
                    total_stack[0] = i
                    total_stack[1] = sum(mat[i])
                else :
                    continue
            else:
                continue
        return total_stack