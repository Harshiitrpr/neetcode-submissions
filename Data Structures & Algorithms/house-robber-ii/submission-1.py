class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)
        first, second, third = nums[0], nums[1], nums[0] + nums[2]
        ans = third
        for i in range(3,n-1):
            third, second, first = max(first, second) + nums[i], third, second
        ans = max(first,second,third)

        first, second, third = nums[1], nums[2], nums[3] + nums[1]
        for i in range(4,n):
            third, second, first = max(first, second) + nums[i], third, second
        return max(ans, second, first, third)