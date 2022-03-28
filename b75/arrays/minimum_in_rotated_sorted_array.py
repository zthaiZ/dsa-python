class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # utilize binary search
        # array is basically half sorted, find the portion that has the lower end of the sort
        # once we know the sorted portion with smaller numbers, grab that leftmost value
        
        left = 0
        right = len(nums)-1
        res = nums[0]
        
        while (left <= right):
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left+right) // 2
            res = min(res, nums[mid])
            
            if nums[left] <= nums[mid]:
                left = mid+1
            else:
                right = mid-1
                
        return res
        