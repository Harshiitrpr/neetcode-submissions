class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, len(height) - 1
        ans = min(height[i], height[j]) * (j - i)

        while j > i:
            if height[i] < height[j]:
                tmp = height[i]
                while i < n and height[i] <= tmp:
                    i += 1
                if i == n:
                    return ans
                ans = max(ans,  min(height[i], height[j]) * (j - i))
            else:
                tmp = height[j]
                while j >= 0 and height[j] <= tmp:
                    j -= 1
                if j < 0:
                    return ans
                ans = max(ans,  min(height[i], height[j]) * (j - i))
        return ans
        