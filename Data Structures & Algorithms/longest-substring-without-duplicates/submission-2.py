from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        freq = defaultdict(int)
        l, r = 0,0
        n = len(s)
        freq[ord(s[0]) - ord('a')] += 1
        ans = 1
        for r in range(1,n):
            freq[ord(s[r]) - ord('a')] += 1
            while freq[ord(s[r]) - ord('a')] > 1:
                freq[ord(s[l]) - ord('a')] -= 1
                l += 1
            ans = max(r - l + 1, ans)
        return ans
            
        