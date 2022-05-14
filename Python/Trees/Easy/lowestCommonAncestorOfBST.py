class Solution(object):
    def lowestCommonAncestorOfBST(self, root, p, q):
        # init p_val, q_val, parent_node
        p_val = p.val
        q_val = q.val
        parent_node = root.val 

        # condition if p & q > parent_node 
        if (p_val > parent_node and q_val > parent_node):
            return self.lowestCommonAncestorOfBST(root.right, p, q)

        # condition if p & q < parent_node
        if (p_val < parent_node and q_val < parent_node):
            return self.lowestCommonAncestorOfBST(root.left, p, q)

        # return root
        else: 
            return root 
       