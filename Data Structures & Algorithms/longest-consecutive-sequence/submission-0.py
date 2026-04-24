from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        prefix = defaultdict(int)
        suffix = defaultdict(int)
        longest = 0
        for i in nums:
            left = prefix[i-1]
            right = suffix[i+1]
            current = left + right + 1
            longest = max(current, longest)
            suffix[i - left] = max(current, suffix[i - left])
            prefix[i + right] = max(current, prefix[i + right])
        return longest

'''
left = 0, right = 0
current = 1
longest = 1
suffix[1] = 1
[prefix][1] = 1

i = 0,
left = 0
right = 1
current = 2
suffix[0] = 2
prefix[1] = 2

i = 1
left = prefix[0] = 0
right = suffix[2] = 0
current = 1
suffix[0] = 1'''