class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            cell_value = grid[r][c]
            grid[r][c] = 0
        
            return (
                cell_value
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        valid_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    total_value = dfs(r, c)
                    if total_value % k == 0:
                        valid_islands += 1
                        
        return valid_islands