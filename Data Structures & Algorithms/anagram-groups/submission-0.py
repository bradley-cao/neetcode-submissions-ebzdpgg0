class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = dict()
        for i in range(len(strs)):
            chars = ''.join(sorted(strs[i]))
            if chars in lists:
                lists[chars].append(strs[i])
            else:
                lists[chars] = [strs[i]]
        return list(lists.values())