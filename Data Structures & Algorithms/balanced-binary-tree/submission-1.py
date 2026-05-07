# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [root]
        mp = {}
        while stack:
            curr = stack[-1]
            if not curr:
                return 0
            if curr.left and curr.left not in mp:
                stack.append(curr.left)
            elif curr.right and curr.right not in mp:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                left, right = mp.get(curr.left,0), mp.get(curr.right,0)
                mp[curr] = 1 + max(left,right)
                if abs(left - right) > 1:
                    return False
        return True
        