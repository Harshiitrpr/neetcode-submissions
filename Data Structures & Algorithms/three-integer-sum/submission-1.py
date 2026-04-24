class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        first, second, third = 0, 1, n-1 #assuming n > 3
        ans = []

        for first in range(n-2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            tar = -nums[first]
            l, r = first + 1, n - 1
            while l < r:
                if nums[l] + nums[r] < tar:
                    l += 1
                elif nums[l] + nums[r] > tar:
                    r -= 1
                else:
                    ans.append([nums[first], nums[l], nums[r]])
                    l1, r1 = l + 1, r - 1
                    while nums[l1] == nums[l] and nums[r1] == nums[r] and l1 <= r1:
                        l1 += 1
                        r1 -= 1
                    l, r = l1, r1
        return ans

