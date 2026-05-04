class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        ans = 0
        for i in range(n):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    tmp = stack.pop()
                    l= -1
                    if stack:
                        l = stack[-1]
                    ans = max(ans, heights[tmp]*(i - l - 1))
                stack.append(i)
        while stack:
            tmp = stack.pop()
            l= -1
            if stack:
                l = stack[-1]
            ans = max(ans, heights[tmp]*(n  - l - 1))
        return ans