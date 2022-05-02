/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    TreeNode ans = null;
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        this.recurseTree(root, p, q);
        return this.ans;
    }
    
    public boolean recurseTree(TreeNode currentNode, TreeNode p, TreeNode q) {
        if (currentNode == null) {
            return false;
        }
        
        int mid = (currentNode == p|| currentNode == q) ? 1 : 0;
        
        int left = this.recurseTree(currentNode.left,p,q) ? 1 : 0;
        
        int right = this.recurseTree(currentNode.right,p,q) ? 1 : 0;
        
        if (mid + left + right >= 2) {
            this.ans = currentNode;
        }
        
        return (mid + left + right > 0);
    }
    
}
