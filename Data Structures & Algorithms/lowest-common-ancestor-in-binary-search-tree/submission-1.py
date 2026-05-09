# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        tmp = root
        while True:
            if tmp.val < min(p.val, q.val):
                tmp = tmp.right
            elif tmp.val > max(p.val, q.val):
                tmp = tmp.left
            else:
                return tmp