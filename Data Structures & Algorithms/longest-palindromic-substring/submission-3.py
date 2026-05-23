class Solution:
    def longestPalindrome(self, s: str) -> str:
        text = '#' + '#'.join(s) + '#'
        n = len(text)
        p = [0]*n
        center, right = 0, 0
        ans_idx, ans_radius = 0, 0
        for i in range(1,n-1):
            #Case 1: outside palindrome
            if i > right:
                l, r = i, i
                while r + 1 < n and l -1 >= 0 and text[l-1] == text[r + 1]:
                    l -= 1
                    r += 1
                p[i] = r - i
                if r > right:
                    center = i
                    right = r
                if p[i] > ans_radius:
                    ans_idx = i
                    ans_radius = p[i]
                continue
            
            mirror = center - (i - center)
            left = center - (right - center)

            #Case 2a: contained and expands
            if p[mirror] < right - i:
                p[i] = p[mirror]
                continue

            #Case 2b: expands 
            elif p[mirror] > right - i:
                p[i] = right - i
                continue
            
            #Case 3: finishes exactly at righe edge
            else:
                l, r =  i - (right - i), right
                while r + 1 < n and l -1 >= 0 and text[l-1] == text[r + 1]:
                    l -= 1
                    r += 1
                p[i] = r - i
                if r > right:
                    center = i
                    right = r
                if p[i] > ans_radius:
                    ans_idx = i
                    ans_radius = p[i]
                continue
        ans = []
        print(text[ans_idx - ans_radius:ans_idx + ans_radius + 1])
        for i in range(ans_idx - ans_radius + 1, ans_idx + ans_radius, 2):
            ans.append(text[i])
        return ''.join(ans)
            
