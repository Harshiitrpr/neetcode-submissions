import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negs = [-i for i in stones]
        heapq.heapify(negs)
        while len(negs) > 1:
            a = heapq.heappop(negs)
            b =  heapq.heappop(negs)
            if abs(a - b) > 0:
                heapq.heappush(negs,-abs(a-b))
        if len(negs) == 1:
            return -negs[0]
        else:
            return 0