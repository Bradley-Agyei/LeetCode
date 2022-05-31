class Solution(object):
    def redundantConnections(self, edges):
        # union find approach 
        # init parent_list, rank_list
        parent_list = [i for i in range(len(edges) + 1)]
        rank_list = [1] * (len(edges) + 1)

        # find function 
        def find(node):
            # find root_parent
            root_parent = parent_list[node]

            # while root_parent doesn't equal itself
            while root_parent != parent_list[root_parent]:
                # path compression --> sets nodes parent to its grandparent 
                parent_list[root_parent] = parent_list[parent_list[root_parent]]
                root_parent = parent_list[root_parent]
            return root_parent

        # union function --> returns false if cycle is identified
        def union(node1, node2):
            # find parent of nodes 
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return False
            
            # if not change parent of node and update rank list 
            if rank_list[parent1] > rank_list[parent2]:
                parent_list[parent2] = parent1
                rank_list[parent1] += rank_list[parent2]
            else:
                parent_list[parent1] = parent2
                rank_list[parent2] += rank_list[parent1]

            return True 

        # go through all possible edges and return edge that causes cycle 
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]