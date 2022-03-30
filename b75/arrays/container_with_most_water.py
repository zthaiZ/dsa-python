class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxWater = max(maxWater, (right-left)*min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return maxWater