class Solution(object):
    def kthSmallestElement(self, root, k):

        # inorder helper function 
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]

#Time comp: O(n)
#Space comp: O(n)