class Solution(object):
    def isBalanced(self, root):
        # height function (dfs func)
        def height(root):
            # base case if root is empty 
            if not root:
                return [True, 0]

            # find if children are balanced
            left_height = height(root.left)
            right_height = height(root.right)

            # balanced_tree var returns true if tree is balanced 
            balanced_tree = (left_height[0] and right_height[0] and 
                            abs(left_height[1] - right_height[1]) <= 1)

            # return result from balanced_tree and height of tree
            return [balanced_tree, 1 + max(left_height[1], right_height[1])]

        # return result from height function
        return height(root)[0] 