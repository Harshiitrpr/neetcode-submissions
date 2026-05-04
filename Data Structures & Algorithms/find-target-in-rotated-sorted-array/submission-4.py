class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        start = 0
        if nums[0] > nums[-1]:
            l, r = 0, n

            while l < r:
                m = l + (r - l)//2
                if nums[m] >= nums[0]:
                    l = m + 1
                elif nums[m] < nums[0]:
                    r = m
            start = l
        
        if nums[-1] == target:
            return n - 1
        elif nums[-1] < target:
            l, r = 0, start
            while l < r:
                m = l + (r - l)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m
                else:
                    l = m + 1
        else:
            l, r = start, n
            while l < r:
                m = l + (r - l)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m
                else:
                    l = m + 1
        return -1