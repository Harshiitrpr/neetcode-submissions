import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[-x*x - y*y, x, y] for x, y in points]
        heapq.heapify(distances)
        if len(points) < k:
            return []
        while len(distances) > k:
            heapq.heappop(distances)
        
        return [[x,y] for d,x,y in distances]