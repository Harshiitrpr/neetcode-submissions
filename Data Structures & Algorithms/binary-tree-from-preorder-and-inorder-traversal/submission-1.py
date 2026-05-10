# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        idx = {val:idx for idx, val in enumerate(inorder)}
        curr = 0
        def dfs(l, r):
            nonlocal curr
            if r <= l:
                return None
            mid = idx[preorder[curr]]
            root = TreeNode(preorder[curr])
            curr += 1
            root.left = dfs(l, mid)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder))