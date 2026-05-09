# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        ans = []
        while queue:
            curr = []
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp:
                    curr.append(tmp.val)
                    queue.append(tmp.left)
                    queue.append(tmp.right)
            if curr:
                ans.append(curr[-1])
        return ans