class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        min_distance = [[0]*(m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            min_distance[i][0] = i
        
        for j in range(m + 1):
            min_distance[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i - 1] == word2[j - 1]:
                    min_distance[i][j] = min_distance[i-1][j-1]
                
                else:
                    min_distance[i][j] = 1 + min(min_distance[i-1][j], min_distance[i][j-1], min_distance[i-1][j-1])
        
        return min_distance[n][m]
                