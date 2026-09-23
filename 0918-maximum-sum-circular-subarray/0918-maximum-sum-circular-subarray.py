class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = nums[0]
        current_max = nums[0]
        max_sum = nums[0]
        current_min = nums[0]
        min_sum = nums[0]
        for num in nums[1:]:
            total += num 
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)
        while max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
