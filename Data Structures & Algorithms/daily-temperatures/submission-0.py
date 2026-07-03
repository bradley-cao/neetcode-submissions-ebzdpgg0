class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while len(stack) > 0 and temp > stack[-1][0]:
                prevTemp, prevIdx = stack.pop()
                ret[prevIdx] = i - prevIdx
            
            stack.append((temp, i))
        
        return ret
                            
