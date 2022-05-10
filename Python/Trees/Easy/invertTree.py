class Solution(object):
    def invertTree(self, root):
        # if root != none, perform swaps of children 
        if (root != None):
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)

            #Swap children
            root.left = right
            root.right = left

        return root 

#Time comp: O(n)
#Space comp: O(n)