class Solution:
    def minimizedStringLength(self, s: str) -> int:
        a = list(set(s))
        a = "".join(a)
        return len(a)