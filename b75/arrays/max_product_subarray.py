class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #not setting to 0, what if nums is just [-1]
        res = max(nums)
        #initialized to 1, 1 since we are multiplying against this
        curr_max, curr_min = 1, 1
        
        #go through and calculate products while keeping track of maxes and mins
        #keeping track of mins because being mindful of negative negative (i.e. -x * -y = z)
        for num in nums:
            temp = curr_max * num
            curr_max = max(curr_max * num, curr_min * num, num)
            curr_min = min(temp, curr_min * num, num)
            res = max(res, curr_max)
        return res
            