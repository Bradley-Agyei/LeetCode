class Solution(object):
    def graphValidTree(self, n, edges):
        # if not n --> return true
        if not n:
            return True 

        # adjacency list to map nodes with their edges 
        adj_list = {i:[] for i in range(n)}

        # append edges to nodes in adj_list (undirected)
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        # visit set to ensure no cycles 
        visit_set = set()

        # dfs function 
        def dfs(current_node, prev_node):
            # base case --> current_node already visited
            if current_node in visit_set:
                return False 

            # add current_node to visit_set
            visit_set.add(current_node)

            # loop through and check current nodes neighbors
            for neighbor in adj_list[current_node]:
                if neighbor == prev_node:
                    continue 
                if not dfs(neighbor, current_node):                 # cycle has been detected
                    return False 
            return True 

        # return the final result if dfs function returns true 
        return dfs(0, -1) and n == len(visit_set) 
        