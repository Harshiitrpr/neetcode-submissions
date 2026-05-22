class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
        ans = s[0]
        for j in range(1,n):
            for i in range(0, n - j):
                if (j == 1 or dp[i + 1][i + j -1]) and s[i] == s[i + j]:
                    dp[i][i + j] = True
                    if len(ans) < j + 1:
                        ans = s[i:i + j + 1]
                else:
                    dp[i][i + j] = False
        return ans
