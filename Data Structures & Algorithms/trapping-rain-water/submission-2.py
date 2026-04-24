class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        ans = 0
        for i in range(n):
            curr = height[i]
            if not stack or height[stack[-1]] > curr:
                stack.append(i)
            else:
                while stack and height[stack[-1]] <= curr:
                    last = stack.pop()
                    if stack:
                        ans += (min(height[stack[-1]], curr) - height[last])* (i - stack[-1] - 1)
                stack.append(i)
        return ans


