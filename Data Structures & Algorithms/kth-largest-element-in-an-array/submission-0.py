class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minheap = []
        for i in nums:
            heapq.heappush(minheap, i)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return heapq.heappop(minheap)
