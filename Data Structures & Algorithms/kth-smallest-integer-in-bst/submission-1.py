# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #morris traversal
        if not root:
            return -1
        
        curr = root
        count = k
        while curr:
            if curr.left == None:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                tmp = curr.left
                while tmp.right and tmp.right != curr:
                    tmp = tmp.right

                if tmp.right == None:
                    tmp.right = curr
                    curr = curr.left
                else:
                    tmp.right = None
                    k -= 1
                    
                    if k == 0:
                        return curr.val
                    curr = curr.right
            