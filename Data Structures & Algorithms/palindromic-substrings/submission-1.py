class Solution:
    def countSubstrings(self, s: str) -> int:
        text = '#' + '#'.join(s) + '#'
        n = len(text)
        P = [0]*n
        center, right = 0,0
        ans = 0
        for i in range(1,n-1):
            # Case 1: Outside palindrome
            if i > right:
                l, r = i,i
                while l-1 >=0 and r + 1 < n and text[l-1] == text[r+1]:
                    l -= 1
                    r += 1
                P[i] = r - i
                ans += (P[i] + 1)//2
                center, right = i, r
                continue
            
            # Case 2: contained in palindrome
            mirror = center - (i - center)
            if i + P[mirror] < right:
                P[i] = P[mirror]
                ans += (P[i] + 1)//2
                continue
            
            # Case 3: exceeds border
            if i + P[mirror] > right:
                P[i] = right - i
                ans += (P[i] + 1)//2
                continue
            
            # Case 4: touching border
            else:
                l, r = i - (right - i), i + right - i
                while l-1 >=0 and r + 1 < n and text[l-1] == text[r+1]:
                    l -= 1
                    r += 1
                P[i] = r - i
                center, right = i, r
                ans += (P[i] + 1)//2
                continue
        return ans        
