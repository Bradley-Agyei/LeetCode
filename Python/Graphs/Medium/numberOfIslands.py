class Solution(object):
    def islands(self, grid):
        # init islands, visited set, rows/cols of grid
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        # case to see if grid is empty 
        if not grid:
            return 0 

        # dfs function 
        def dfs(r, c):
            # conditions that will return nothing 
            if (r not in range(rows) or
                c not in range(cols) or 
                grid[r][c] == "0" or 
                (r,c) in visited):
                return 

            visited.add((r,c))
            # check all 4 directions 
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # iterate through entire grid and update number of islands 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
        return islands