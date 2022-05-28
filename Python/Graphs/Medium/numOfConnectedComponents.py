class Solution(object):
    def connectedComponents(self, n, edges):
        # init num_of_connected_components
        num_of_connected_components = n 

        # parent_list that initially only has each node from given input 
        parent_list = {i for i in range(n)}
        # rank list 
        rank = [1] * n 

        # find function - find the root_parent of a node 
        def find(n1):
            # root parent of node is initially itself 
            root_parent = n1 

            while root_parent != parent_list[root_parent]:
                # path compression - set root parent to nodes grandparent if it has one
                parent_list[root_parent] = parent_list[parent_list[root_parent]]             
                root_parent = parent_list[root_parent]
            return root_parent 

        # union function 
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0 
            if rank[p2] > rank[p1]:
                parent_list[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent_list[p2] = p1
                rank[p1] += rank[p2]
            return 1 

        # loop through all edges
        for n1, n2 in edges:
            num_of_connected_components -= union(n1, n2)
        return num_of_connected_components