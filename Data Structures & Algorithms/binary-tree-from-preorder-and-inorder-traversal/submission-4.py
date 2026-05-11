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
        i, j, n = 0, 0, len(preorder)
        curr = TreeNode(0)
        head = curr
        while i < n and j < n:
            #go right and as left as possible
            curr.right = TreeNode(preorder[i], right=curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                i += 1
                curr = curr.left
            j += 1
            while j < n and curr.right and curr.right.val == inorder[j]:
                prev = curr
                curr = curr.right
                prev.right = None
                j += 1
        return head.right
