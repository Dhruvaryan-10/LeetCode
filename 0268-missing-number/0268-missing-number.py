class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        result = n
        for i, num in enumerate(nums):
            result ^= i
            result ^= num
        return result