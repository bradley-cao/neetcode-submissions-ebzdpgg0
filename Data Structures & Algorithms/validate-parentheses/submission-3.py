class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lefts = {"{", "(", "["}
        for i in range(len(s)):
            paren = s[i]
            if paren in lefts:
                stack.append(paren)
            elif len(stack) > 0:
                if paren == "}" and stack[-1] == "{":
                    stack.pop()
                elif paren == "]" and stack[-1] == "[":
                    stack.pop()
                elif paren == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return len(stack) == 0