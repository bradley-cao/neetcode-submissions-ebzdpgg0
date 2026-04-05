class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shareLength = min(len(word1), len(word2))
        ans = ""
        for i in range(shareLength):
            ans += word1[i]
            ans += word2[i]
        
        if len(word1) > shareLength:
            ans += word1[shareLength:]
        else:
            ans += word2[shareLength:]

        return ans