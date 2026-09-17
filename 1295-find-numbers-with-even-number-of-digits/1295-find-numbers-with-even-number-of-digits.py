class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        result = 0
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        result = count 
        return count 