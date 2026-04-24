class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        freq = [0]*100
        l, r = 0,0
        n = len(s)
        freq[ord(s[0]) - ord(' ')] += 1
        ans = 1
        for r in range(1,n):
            freq[ord(s[r]) - ord(' ')] += 1
            while freq[ord(s[r]) - ord(' ')] > 1:
                freq[ord(s[l]) - ord(' ')] -= 1
                l += 1
            ans = max(r - l + 1, ans)
        return ans
            
        