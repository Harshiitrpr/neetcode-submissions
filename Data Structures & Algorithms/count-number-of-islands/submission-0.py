class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        def bfs(a, b):
            queue = deque([[a,b]])
            while queue:
                x, y = queue.popleft()
                grid[x][y] = "2"
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == "1":
                        queue.append([x + dx, y + dy])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    ans += 1
                    bfs(i, j)
        return ans
                        