class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        for c in range(1, n):
            dp[c] = {val ^ grid[0][c] for val in dp[c - 1]}
        for r in range(1, m):
            new_dp = [set() for _ in range(n)]
            new_dp[0] = {val ^ grid[r][0] for val in dp[0]}
            for c in range(1, n):
                combined_prev = dp[c] | new_dp[c - 1]
                new_dp[c] = {val ^ grid[r][c] for val in combined_prev}
            dp = new_dp   
        return min(dp[n - 1])