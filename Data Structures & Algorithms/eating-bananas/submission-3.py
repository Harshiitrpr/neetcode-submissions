class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n > h:
            return "not possible"
        l, r = 1, max(piles)
        ans = r
        while l < r:
            m = l + (r - l)//2
            hours = 0
            for p in piles:
                hours += (p + m - 1)//m
            if hours > h:
                l = m + 1
            else:
                r = m
                ans = min(ans, m)
        return ans