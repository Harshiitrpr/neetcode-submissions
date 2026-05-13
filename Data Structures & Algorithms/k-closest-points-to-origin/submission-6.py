import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        # if k == n:
        #     return points
        distance = lambda x: x[0]*x[0] + x[1]* x[1]
        def partition(l, r, pivot_index):
            points[r], points[pivot_index] = points[pivot_index], points[r]

            pivot = distance(points[r])
            ans = l
            for i in range(l,r):
                if distance(points[i]) <= pivot:
                    points[i], points[ans] = points[ans], points[i]
                    ans += 1
            points[ans], points[r] = points[r], points[ans]
            
            return ans
        
        l, r = 0, n -1
        pivot = n
        while pivot != k:
            m = (l + r)//2
            pivot = partition( l, r, m)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:k]