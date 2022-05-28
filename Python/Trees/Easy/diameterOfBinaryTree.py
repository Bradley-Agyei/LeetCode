class Solution(object):
    def diameterOfBT(self, root):
        # init diameter to 0
        diameter = 0 

        # dfs function 
        def longestPath(node):
            # base case 
            if not node:
                return 0 

            # nonlocal diameter 
            nonlocal diameter 

            # find the length of the left and right children 
            left_path = longestPath(node.left)
            right_path = longestPath(node.right)

            # set diameter 
            diameter = max(diameter, left_path + right_path)

            # return max 
            return max(left_path, right_path) + 1 

        # call longestPath 
        longestPath(root)
        return diameter 

