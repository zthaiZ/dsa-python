class Solution:
    def productExceptSelf(self, nums):
        #initialize output array
        res = [1] * len(nums)
        
        #prefix of the 1st index is 1 (nothing to the left of the first value)
        prefix = 1
        
        #looping through and calculating the products from left to right into res
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1    
        #looping through and calculating products from right to left into res
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix #multiple postfix and the prefix that has been set there via loop above
            postfix*=nums[i]
            
        return res