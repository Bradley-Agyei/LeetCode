/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isBST(root, null, null);
        
    }
    
    public boolean isBST(TreeNode root, Integer lo, Integer hi) {
        if(root == null)
            return true;
        
        if(hi != null && root.val >= hi)
            return false;
        
        if(lo != null && root.val <= lo)
            return false;
        
        return isBST(root.left, lo, root.val) && isBST(root.right, root.val, hi);
    }
}


