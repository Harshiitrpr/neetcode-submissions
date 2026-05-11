# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(node):
            if not node:
                ans.append("N")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(",")
        i, n = 0, len(preorder)
        def dfs():
            nonlocal i
            if not preorder[i] or preorder[i] == "N":
                i += 1
                return None
            res = TreeNode(int(preorder[i]))
            i += 1
            res.left = dfs()
            res.right = dfs()
            return res
        return dfs()


