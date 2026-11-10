class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):
            cost_j = costs[j - 1]
            for i in range(max(0, j - 3), j):
                dp[j] = min(dp[j], dp[i] + cost_j + (j - i) ** 2)
                
        return dp[n]