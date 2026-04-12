class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + "#" + word
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        numstr = ""
        while i < len(s):
            if s[i] == "#":
                if len(numstr) == 0:
                    res.append(s[i])
                else:
                    i += 1
                    length = int(numstr)
                    word = ""
                    for j in range(length):
                        word += s[i]
                        i += 1
                    res.append(word)
                    numstr = ""
            else:
                numstr += s[i]
                i += 1
        
        return res