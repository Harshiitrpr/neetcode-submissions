class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        level = 0
        ans = 0
        while l < r:
            if height[l] < height[r]:
                level = max(height[l], level)
                ans += level - height[l]
                l += 1
            else:
                level = max(height[r], level)
                ans += level - height[r]
                r -= 1
        return ans
