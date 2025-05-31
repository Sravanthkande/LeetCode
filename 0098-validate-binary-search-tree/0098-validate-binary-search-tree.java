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
    private boolean validate(TreeNode node, long minVal, long maxVal){
        if(node == null) return true;

        if(node.val <= minVal || node.val >= maxVal) return false;

        boolean left = validate(node.left, minVal, node.val);
        boolean right = validate(node.right, node.val, maxVal);

        return left && right;
    }
    public boolean isValidBST(TreeNode root) {
        return validate(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}