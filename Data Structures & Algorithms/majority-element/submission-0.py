class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        return max(counts, key=counts.get)