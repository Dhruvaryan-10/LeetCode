class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def backtrack(current, open_count, closed_count):
            if len(current) == 2 * n:
                result.append(current)
                return 
            if open_count < n:
                backtrack(
                    current + "(",
                    open_count + 1,
                    closed_count
                )
            if closed_count < open_count:
                backtrack(
                    current + ")",
                    open_count,
                    closed_count + 1
                )
        backtrack("", 0, 0)
        return result
