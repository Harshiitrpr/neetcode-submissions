class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        node = root
        
        while node:
            # If both p and q are greater than parent
            if p_val > node.val and q_val > node.val:
                node = node.right
                
            # If both p and q are lesser than parent
            elif p_val < node.val and q_val < node.val:
                node = node.left
                
            # We have found the split point, i.e. the LCA node
            else:
                return node