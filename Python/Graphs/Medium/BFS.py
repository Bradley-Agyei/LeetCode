from collections import deque 

class Solution(object):
    def BFS(self, node, graph, visited):

        # visited set to keep track of nodes we've already seen 
        visited_set = set()

        # queue DS
        queue = deque() 

        # add our node to visited_set and queue 
        visited_set.add(node)
        queue.append(node)

        # condition: while queue is not empty 
        while queue:
            # pop left most node 
            node = queue.popleft()

            # check neighbors 
            for neighbor in graph[node]:
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    queue.append(neighbor)