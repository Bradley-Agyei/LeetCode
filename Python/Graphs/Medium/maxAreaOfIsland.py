class Solution(object):
    def maxAreaOfIsland(self, grid):
        # init rows, cols, max_area, visited_set
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited_set = set()

        # dfs recursive function
        def islandCount(r,c):
            # base case 
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                grid[r][c] == 0 or
                (r,c) in visited_set):
                return 0 

            # add cell to visited_set
            visited_set.add((r,c))

            # check all four directions 
            return (1 + islandCount(r + 1, c) +
                        islandCount(r - 1, c) +
                        islandCount(r, c + 1) +
                        islandCount(r, c - 1)) 
        
        # iterate through rows and cols and return max_area
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, islandCount(r,c))
        return max_area 
        