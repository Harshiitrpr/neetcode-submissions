# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def lps(self, pat):
        n = len(pat)
        lps = [0]*n
        i, j = 1, 0
        while i < n:
            if pat[i] == pat[j]:
                j += 1
                lps[i] = j
                i += 1
            elif j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
    
    def kmp(self, pat, text):
        lps = self.lps(pat)
        m,n = len(text), len(pat)
        i, j = 0, 0
        while i < m and j < n:
            if text[i] == pat[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        if j == n:
            return True
        else: 
            return False
    
    def lengthen(self, root: Optional[TreeNode]):
        if not root:
            return ""
        stack = [root]
        ans = ""
        while stack:
            curr = stack.pop()
            if not curr:
                ans += "$#"
                continue
            ans += "$" + str(curr.val)
            stack.append(curr.left)
            stack.append(curr.right)
        return ans


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        s1, s2 = self.lengthen(root), self.lengthen(subRoot)
        print(s1, s2)
        if self.kmp(s2, s1):
            return True
        else:
            return False
        

        