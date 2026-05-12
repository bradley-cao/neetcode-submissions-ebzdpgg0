class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        minheap = []
        for num in count:
            heapq.heappush(minheap, (count[num], num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(minheap)[1])
        
        return ans