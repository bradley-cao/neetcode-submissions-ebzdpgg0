class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 0
                tmp = num
                while tmp in numSet:
                    tmp += 1
                    length += 1
                longest = max(length, longest)
        
        return longest