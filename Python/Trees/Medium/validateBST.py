class Solution(object):
    def validateBST(self, root):

        # define validate BST function 
        def validate(node, low=float("-inf"), high=float("inf")):
            # base case
            if not node:
                return True 

            # condition to check whether in bounds 
            if (node.val <= low or node.val >= high):
                return False 

            # check both left and right children 
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        validate(root)

#Time comp: O(n)
#Space comp: O(n)
