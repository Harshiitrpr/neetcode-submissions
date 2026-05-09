# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        tmp = root
        small, big = min(p.val, q.val), max(p.val, q.val)
        while tmp:
            if tmp.val < small:
                tmp = tmp.right
            elif tmp.val > big:
                tmp = tmp.left
            else:
                return tmp