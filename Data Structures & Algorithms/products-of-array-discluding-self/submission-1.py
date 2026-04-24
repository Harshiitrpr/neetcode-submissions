class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1]
        suffix_prod = [1]
        for i in nums:
            prefix_prod.append(prefix_prod[-1]*i)
        for i in reversed(nums):
            suffix_prod.append(suffix_prod[-1]*i)
        
        ans = []
        n = len(nums)
        for i in range(n):
            ans.append(prefix_prod[i] * suffix_prod[n - i - 1])
        return ans

        

        