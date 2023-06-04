class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = list(num)
        k = 0
        while k == 0:
            i = 0
            if num[-(i+1)] == "0":
                num.pop()
                i += 1
            else :
                k += 1
        return "".join(num)