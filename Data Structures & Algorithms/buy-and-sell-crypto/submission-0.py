class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        ans = 0
        currmin = prices[0]
        for curr in prices:
            ans = max(ans, curr - currmin)
            currmin = min(currmin, curr)
        return ans