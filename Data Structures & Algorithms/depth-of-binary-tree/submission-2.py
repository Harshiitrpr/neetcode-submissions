# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # level wise bfs
        if not root:
            return 0
        ans = 0
        queue = deque([root])

        while queue:
            flag = False
            for _ in range(len(queue)):
                curr = queue.pop()
                if curr:
                    queue.appendleft(curr.left)
                    queue.appendleft(curr.right)
                    flag = True
            if flag:
                ans += 1
        return ans
