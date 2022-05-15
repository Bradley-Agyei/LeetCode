class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        # base case 
        if not preorder or not inorder:
            return None 

        # grab root in preorder 
        root = TreeNode(preorder[0])

        # find index of root in inorder 
        mid = inorder.index(preorder[0])

        # build left and right side of tree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return built tree
        return root 

#Time comp: O(n)
#Space comp: O(n)