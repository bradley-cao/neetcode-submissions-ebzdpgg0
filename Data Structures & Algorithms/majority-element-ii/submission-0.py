class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = dict()
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        res = []
        for num in counts:
            if counts[num] > len(nums) // 3:
                res.append(num)

        return res
        