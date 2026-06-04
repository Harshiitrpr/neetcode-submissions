import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        if not (heights and heights[0]):
            return -1
        n, m = len(heights), len(heights[0])
        heap = [[0, (0,0)]]  
        dis = [[float('inf')]*m for _ in range(n)]
        dis[0][0] = 0
        while heap:
            cur_dis, (x, y)= heapq.heappop(heap)
            if cur_dis > dis[x][y]:
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m and dis[new_x][new_y] > max(dis[x][y], abs(heights[x][y] - heights[new_x][new_y])):
                    dis[new_x][new_y] = max(dis[x][y], abs(heights[x][y] - heights[new_x][new_y]))
                    heapq.heappush(heap, [dis[new_x][new_y], (new_x, new_y)])
        return dis[n-1][m-1]