class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        maximum = 0
        while left < right:
            width = right - left
            current_area = width * min(height[left], height[right])
            maximum = max(maximum, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum 