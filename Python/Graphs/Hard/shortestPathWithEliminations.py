from collections import deque 

class Solution(object):
    def shortestPath(self, grid, k): 
        # rows, cols, target_cell, seen_set, state, queue DS
        rows, cols = len(grid), len(grid[0])
        target_cell = (rows - 1, cols - 1)

        # edge case: if we have an unlimited number of k to find shortest path 
        if k >= rows + cols - 2:
            return rows + cols - 2

        # state --> (rows, cols, # of eliminations)
        state = [(0, 0, k)]

        # queue 
        queue = deque([(0, state)])

        # seen set 
        seen_set = set([state])

        # directions for all 4 options 
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # start BFS
        while queue:
            #popleft from queue 
            steps, (row, col, k) = queue.popleft()

            # if target cell is reached 
            if (row, col) == target_cell:
                return steps 

            # check all four directions of new node 
            for diff_row, diff_col in directions:
                new_row = row + diff_row
                new_col = col + diff_col 
            
                # ensure new row and new col is in bound set up remaining_k and new state 
                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    remaining_k = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, remaining_k)

                    # check to see if cell qualifies and add to set and queue 
                    if remaining_k >= 0 and new_state not in seen_set:
                        seen_set.add(new_state)
                        queue.append((steps + 1, new_state))

        return -1 

# Time comp: O(n * k)
# Space comp: O(n * k)





        