class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for word in strs:
            key = ''.join(sorted(word))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
        
        ans = []
        for key in anagrams:
            ans.append(anagrams[key])
        
        return ans