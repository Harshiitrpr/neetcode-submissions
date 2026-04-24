from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxlen = 0
        for i in nums_set:
            if i - 1 not in nums_set:
                length = 1
                tmp = i + 1
                while tmp in nums_set:
                    length += 1
                    tmp += 1
                maxlen = max(maxlen, length)
        return maxlen
