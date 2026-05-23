class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1]*(amount + 1)
        dp[0] = 0
        coins.sort()
        for i in range(1,amount+1):
            curr = i + 1
            for coin in coins:
                if i - coin >=0:
                    if dp[i-coin] != -1:
                        curr = min(curr, dp[i-coin] + 1)
                else:
                    break
            if curr < i + 1:
                dp[i] = curr
        return dp[amount]