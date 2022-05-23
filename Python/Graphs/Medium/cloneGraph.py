# node object 
class Node(object):
    def __init__(self, val=0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] 


class Solution(object):
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        # base case if not node
        if not node:
            return node 
        
        # if node is already in visited, return node 
        if node in self.visited:
            return self.visited[node]

        # if not create a new cloned node 
        clone_node = Node(node.val, [])

        # place cloned node in hashmap. original node (key) --> cloned node (value)
        self.visited[node] = clone_node 

        # iterate through neighbors and generate clones 
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node  

        