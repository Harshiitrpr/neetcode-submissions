import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x,y in points:
            heapq.heappush(res, [-x*x -y*y, x, y])
            if len(res) > k:
                heapq.heappop(res)
        
        return [[x,y] for d,x,y in res]