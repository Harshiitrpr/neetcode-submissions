# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 1. Base case: Check node VALUES, not the objects themselves
        if not root or root.val == p.val or root.val == q.val:
            return root
        
        # 2. Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 3. If both left and right returned a node, the current root is the LCA
        if left and right:
            return root
        
        # 4. Otherwise, pass up whichever side found a target
        return left if left else right