class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] #assuming length is at least 1
        n = len(nums)
        suffix = 1
        for i in range(n-1):
            ans.append(ans[-1]*nums[i])
        for i in range(n-2,-1, -1):
            suffix *= nums[i + 1]
            ans[i] *= suffix
        
        return ans

        

        