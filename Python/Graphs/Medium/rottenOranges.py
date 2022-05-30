from collections import deque 
class Solution(object):
    def rottenOranges(self, grid):
        # init rows, cols, fresh_oranges, time, queue DS
        rows, cols = len(grid), len(grid[0])
        fresh_oranges, time = 0, 0

        queue = deque()

        # do some prework to get total number of fresh oranges and add rotten oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        
        # 4 directions 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue and fresh_oranges > 0:
            queue_length = len(queue)
            for i in range(queue_length):
                r, c = queue.popleft()

                # check all four directions of rotten orange
                for dr, dc in directions:
                    row, col = r + dr, c + dc 

                    # mark direct neighbors of rotten orange as rotten 
                    if (row in range(rows) and 
                        col in range(cols) and
                        grid[row][col] == 1):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh_oranges -= 1
            time += 1
        return time if fresh_oranges == 0 else -1 
