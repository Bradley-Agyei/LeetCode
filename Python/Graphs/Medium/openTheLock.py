from collections import deque 
class Solution(object):
    def openLock(self, deadends, target):
        # base case 
        if "0000" in deadends:
            return -1
        
        # queue DS --> (lock, turns)
        queue = deque([("0000", 0)])

        # visited_set --> (deadends)
        visited_set = set(deadends)
        
        # childLocks function 
        def childLocks(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                result.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10) 
                result.append(lock[:i] + digit + lock[i+1:])
            return result 

        # run bfs using queue
        while queue:
            lock, turns = queue.popleft()

            # if target is found 
            if lock == target:
                return turns 
            
            # check the "sublocks"
            for child in childLocks(lock):
                if child not in visited_set:
                    visited_set.add(child)
                    queue.append((child, turns + 1))
        return -1 

# Time comp: O(N^2 * A^n * D) --> N = num of digits in lock, A = num of digits in alphabet, D = size of deadends
# space comp: O(A^N * D)