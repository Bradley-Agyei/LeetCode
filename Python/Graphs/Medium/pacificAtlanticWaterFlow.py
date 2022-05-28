class Solution(object):
    def pacificAtlantic(self, heights):
        # base case if heights is empty 
        if not heights or not heights[0]:
            return []

        # init rows, cols, pacific/atlantic sets
        num_rows, num_cols = len(heights), len(heights[0])
        pacific_reachable, atlantic_reachable = set(), set()

        # dfs function 
        def dfs(row, col, reachable):
            # mark cell as reachable
            reachable.add((row,col))

            # check all four directions for new cell 
            for (x,y) in [(1,0), (0,1), (-1,0), (0, -1)]:
                new_row, new_col = row + x, col + y

                # check to make sure new cell is within bounds 
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue 

                # check to see if new cell is already in reachable set 
                if (new_row, new_col) in reachable:
                    continue 

                # check to see if old cell can flow into new cell 
                if heights[new_row][new_col] < heights[row][col]:
                    continue

                # recursively call dfs function 
                dfs(new_row, new_col, reachable)

        # iterate the entire height matrix (rows and cols)
        for i in range(num_rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, num_cols - 1, atlantic_reachable)

        for i in range(num_cols):
            dfs(0, i, pacific_reachable)
            dfs(num_rows - 1, i, atlantic_reachable)

        # return the intersection of the sets
        return list(pacific_reachable.intersection(atlantic_reachable))
        

#Time comp: O(M * N)