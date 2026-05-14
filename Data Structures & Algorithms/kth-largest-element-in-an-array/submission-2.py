class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def partition(l, r, pivotindex):
            i, j = l - 1, r + 1
            pivotvalue = nums[pivotindex]
            while i < j:
                i += 1
                while nums[i] < pivotvalue:
                    i += 1
                j -= 1
                while nums[j] > pivotvalue:
                    j -= 1
                
                if i >= j:
                    return j
                nums[i], nums[j] = nums[j], nums[i]
            return j
        k = n-k 
        l, r = 0, n-1
        while l < r:
            split = partition(l, r, l)
            if k <= split:
                r = split
            else:
                l = split + 1
        return nums[r]
                        
