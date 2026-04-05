class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = sorted(''.join(s))
        t_chars = sorted(''.join(t))
        return s_chars == t_chars