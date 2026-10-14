class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(num * num for num in nums)
        result = 0

        for i, square in enumerate(squares):
            if i < len(squares) // 2:
                result -= square
            else:
                result += square

        return result