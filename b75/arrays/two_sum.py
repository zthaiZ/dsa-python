class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return two indices, use two pointers to check pairs that sum up to target
        #X + Y = target ---> X = target - Y
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            seen[nums[i]] = i
        return
