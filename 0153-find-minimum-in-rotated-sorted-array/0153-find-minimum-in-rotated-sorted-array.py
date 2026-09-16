class Solution:
    def findMin(self, nums: list[int]) -> int:
        minimum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                minimum = nums[i]
                break
        return minimum