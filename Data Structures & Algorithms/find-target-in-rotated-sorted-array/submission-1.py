class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        if nums[-1] == target:
            return n-1
        l, r = 0, n-1
        while l < r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif nums[-1] < nums[0] <= nums[m]: # m is in in larger segment
                if nums[m] > target:
                    if target >= nums[0]:
                        r = m
                    else:
                        l = m + 1
                else:
                    l = m + 1
            else:
                if nums[m] > target:
                    r = m
                else:
                    if target <= nums[-1]:
                        l = m + 1
                    else:
                        r = m

        if nums[l] == target:
            return l
        return -1