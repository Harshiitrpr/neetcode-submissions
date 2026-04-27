class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        for ch in s1:
            freq[ch] += 1

        
        freq2 = defaultdict(int)
        l, r = 0, 0

        for r in range(len(s2)):
            freq2[s2[r]] += 1
            if r - l + 1 > len(s1):
                freq2[s2[l]] -= 1
                l += 1
            
            if r - l + 1 == len(s1):
                match = True
                for ch in freq.keys():
                    if freq[ch] != freq2[ch]:
                        match = False
                        break
                if match:
                    return True
        return False

        