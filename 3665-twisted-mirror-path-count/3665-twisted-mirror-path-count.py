class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        dp_right = [[0] * n for _ in range(m)]
        dp_down = [[0] * n for _ in range(m)]
        if 0 < n:
            dp_right[0][0] = 1
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    if c + 1 < n:
                        dp_right[r][c + 1] = (dp_right[r][c + 1] + 1) % MOD
                    if r + 1 < m:
                        dp_down[r + 1][c] = (dp_down[r + 1][c] + 1) % MOD
                    continue
                if grid[r][c] == 0:
                    total = (dp_right[r][c] + dp_down[r][c]) % MOD
                    if total == 0:
                        continue
                    if c + 1 < n:
                        dp_right[r][c + 1] = (dp_right[r][c + 1] + total) % MOD
                    if r + 1 < m:
                        dp_down[r + 1][c] = (dp_down[r + 1][c] + total) % MOD
                else:
                    if dp_right[r][c] > 0 and r + 1 < m:
                        dp_down[r + 1][c] = (dp_down[r + 1][c] + dp_right[r][c]) % MOD
                    if dp_down[r][c] > 0 and c + 1 < n:
                        dp_right[r][c + 1] = (dp_right[r][c + 1] + dp_down[r][c]) % MOD
        return (dp_right[m - 1][n - 1] + dp_down[m - 1][n - 1]) % MOD