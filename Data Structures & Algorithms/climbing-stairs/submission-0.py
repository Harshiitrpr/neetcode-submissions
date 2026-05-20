class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        c = 2
        if n < 2:
            return 1
        for i in range(n-1):
            c = a + b
            b, a = c, b
        return c