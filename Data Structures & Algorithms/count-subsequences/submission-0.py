class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        t_size = len(t)
        mem = [0]*(t_size + 1)
        mem[0] = 1

        for char in s:
            for i in range(t_size, 0, -1):
                if char == t[i-1]:
                    mem[i] += mem[i-1]
        return mem[t_size]