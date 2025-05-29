/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    TreeNode* recursive(TreeNode* node, int val){
        if(node == nullptr){
            return new TreeNode(val);
        }
        if(val < node->val){
            node-> left = recursive(node->left, val);
        }else if(val > node->val){
            node-> right = recursive(node->right, val);
        }

        return node;
    }
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        return recursive(root, val);
    }
};