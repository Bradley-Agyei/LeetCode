class Solution(object):
    def goodNodes(self, root):
        # dfs function to get count of good nodes
        def countGoodNodes(node, max_value):
            # base case 
            if not node:
                return 0 

            # number of good nodes 
            number_of_good_nodes = 1 if node.val >= max_value else 0
            # update our max_value
            max_value = max(max_value, node.val)

            # recursively call function on children and add to number of good nodes 
            number_of_good_nodes += countGoodNodes(node.left, max_value)
            number_of_good_nodes += countGoodNodes(node.right, max_value)

            return number_of_good_nodes

        return countGoodNodes(root, root.val)
