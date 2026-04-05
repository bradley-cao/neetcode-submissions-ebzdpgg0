class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for word in strs:
            key = ''.join(sorted(list(word)))
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        
        ret = []
        for word in anagrams:
            ret.append(anagrams[word])
        
        return ret
        