class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(pre), len(strs[i])) and strs[i][j] == pre[j]:
                j += 1
            pre = pre[:j]
        return pre

