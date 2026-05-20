class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        if n < 2:
            return 1
        for i in range(n-1):
            b, a = a + b, b
        return b