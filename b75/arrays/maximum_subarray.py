class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #not returning actual subarray or range of indices etc, just the sum
        #keep track of a running sum, maximize the sum 
        if not nums:
            return None
        
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum < 0:
                curr_sum = 0
            max_sum = max(max_sum, curr_sum)
            
        return max_sum