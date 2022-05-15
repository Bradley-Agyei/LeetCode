class Solution(object):
    def isSubtree(self, root, subRoot):
        # base case if not root
        if not root:
            return False
        # base case if not subroot
        if not subRoot:
            return True 

        # if sameTree returns True
        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    # helper function sameTree
    def sameTree(self, root, subRoot):
        # base case to see if both trees are empty
        if not root and not subRoot:
            return True

        # case to see if same tree
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        return False