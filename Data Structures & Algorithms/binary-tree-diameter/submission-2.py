# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        # iterative dfs
        if not root:
            return 0
        stack = [root]
        mp = {}
        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in mp:
                stack.append(curr.left)
                
            elif curr.right and curr.right not in mp:
                stack.append(curr.right)

            else:
                curr = stack.pop()
                left, right = mp.get(curr.left,0), mp.get(curr.right, 0)
                mp[curr] = 1 + max(left, right)
                ans = max(ans, left + right)

        return ans



