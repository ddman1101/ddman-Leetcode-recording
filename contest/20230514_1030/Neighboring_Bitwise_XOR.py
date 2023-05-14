class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if derived == [1]:
            return False
        elif derived == [0]:
            return True
        else :
            original = []
            temp = 0
            n = len(derived)
            for i in range(n):
                if i == 0:
                    if (temp ^ 0) == derived[i]:
                        original.append(temp)
                        original.append(0)
                        temp = 0
                    elif (temp ^ 1) == derived[i]:
                        original.append(temp)
                        original.append(1)
                        temp = 1
                elif (i != 0) & (i != (n-1)) :
                    if (temp ^ 0) == derived[i]:
                        original.append(0)
                        temp = 0
                    elif (temp ^ 1) == derived[i]:
                        original.append(1)
                        temp = 1
                elif (i == (n-1)):
                    if (temp ^ original[0]) == derived[n-1]:
                        original = original
                    else :
                        original = []

        if original:
            return True
        else:
            return False