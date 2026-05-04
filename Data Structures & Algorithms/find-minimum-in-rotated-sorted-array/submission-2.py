class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] <= nums[-1]:
            return nums[0]
        l, r = 0, n-1
        while l < r:
            m = l + ( r - l + 1)//2
            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] > nums[0]:
                l = m
            elif nums[m] < nums[0]:
                r = m - 1
        # return nums[r]