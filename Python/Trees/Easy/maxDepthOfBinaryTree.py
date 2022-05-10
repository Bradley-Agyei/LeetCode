class Solution(object):
    def maxDepth(self, root):
        # base case
        if not root:
            return 0
        else:
            # recursive call to find height on both sides of root
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)

        #Return max depth 
        return max(left_height, right_height) + 1


#Time comp: O(n)
#Space comp: O(n)