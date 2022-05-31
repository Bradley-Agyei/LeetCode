from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        # init rows, cols, visited_set, queue DS
        rows, cols = len(rooms), len(rooms[0])
        visited_set = set()
        distance_from_gate = 0 
        queue = deque()

        # add room helper function 
        def addRoom(r,c):
            # conditions that return nothing 
            if (r < 0 or r == rows or
                c < 0 or c == cols or
                rooms[r][c] == -1):
                return 

            visited_set.add((r,c))
            queue.append([r,c])

        # prework to add gates to queue 
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append([r,c])
                    visited_set.add((r,c))

        # execute while queue isn't empty
        while queue:
            queue_length = len(queue)
            for i in range(queue_length):
                r, c = queue.popleft()
                rooms[r][c] = distance_from_gate 
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            distance_from_gate += 1



