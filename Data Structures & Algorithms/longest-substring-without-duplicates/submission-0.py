class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        
        lastindex = dict()

        l = 0
        r = 0

        while r < len(s):
            if s[r] not in lastindex:
                lastindex[s[r]] = r
                r += 1
                maxLen = max(maxLen, r - l)
            elif lastindex[s[r]] < l:
                lastindex[s[r]] = r
                r += 1
                maxLen = max(maxLen, r - l)
            else:
                l += 1
                maxLen = max(maxLen, r - l)
        
        return maxLen

            