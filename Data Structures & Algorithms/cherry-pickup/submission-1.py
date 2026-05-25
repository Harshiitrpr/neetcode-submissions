class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1 or grid[n-1][n-1] == -1:
            return 0
        
        dp = [[float('-inf')]*n for i in range(n)]
        dp[0][0] = grid[0][0]

        for rc in range(1,2*n-1):
            new_dp = [[float('-inf')]*n for i in range(n)]
            for r in range(max(0, rc - (n-1)), min(rc + 1, n)):
                r1, c1 = r, rc - r
                
                for r2 in range(max(0, rc - (n-1)), min(rc + 1, n)):
                    c2 = rc - r2
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue
                    new_dp[r1][r2] = grid[r1][c1]
                    new_dp[r1][r2] += (r1 != r2)*grid[r2][c2]
                    prevs = [[0, 1], [1, 0]]
                    
                    last = float('-inf')
                    for dx, dy in prevs:
                        for dx2, dy2 in prevs:
                            if 0 <= r1 - dx and 0 <= r2 - dx2 and 0 <= c1 - dy and 0 <= c2 - dy2:
                                tmp = dp[r1 - dx][r2 - dx2]
                                last = max(last, tmp)
                    new_dp[r1][r2] += last
            dp = new_dp
        return max(0, dp[n-1][n-1])
