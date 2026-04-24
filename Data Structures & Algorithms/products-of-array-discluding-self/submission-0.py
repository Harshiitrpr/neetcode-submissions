class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = nums.count(0)
        if zeroes > 1:
            return [0 for i in nums]
        elif zeroes == 1:
            prod = 1
            for i in nums:
                if i != 0:
                    prod *= i
            return [0 if i != 0 else prod for i in nums ]
        else:
            prod = 1
            for i in nums:
                prod *= i
            return [prod//i for i in nums]
        