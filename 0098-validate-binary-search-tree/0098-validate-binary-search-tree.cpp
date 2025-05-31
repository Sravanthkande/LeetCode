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
    bool validate(TreeNode* node, long minVal, long maxVal){
        if(node == NULL){
            return true;
        }
        if(node->val <= minVal or node->val >= maxVal){
            return false;
        }

        bool left = validate(node->left, minVal, node->val);
        bool right = validate(node->right, node->val, maxVal);

        return left && right;
    }
public:
    bool isValidBST(TreeNode* root) {
        return validate(root, LONG_MIN, LONG_MAX);
    }
};