class Solution:
    def minLength(self, s: str) -> int:
        k = 0
        i = 0
        while k == 0:
            if (i != (len(s) - 2)) & (len(s) > 1):
                if s[i:i+2] == "AB" or s[i:i+2] == "CD":
                    s = s[0:i] + s[i+2:len(s)]
                    i = 0
                else :
                    s = s
                    i += 1
            elif (i == (len(s) - 2)) & (len(s) > 1):
                if s[i:i+2] == "AB" or s[i:i+2] == "CD":
                    s = s[0:i] + s[i+2:len(s)]
                    i = 0
                else :
                    k += 1
            elif len(s) < 2:
                k += 1
        return len(s)