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
public:
    void inOrderTraversal(TreeNode* root, vector<int>& values){
        if(root){
            inOrderTraversal(root->left, values);
            values.push_back(root->val);
            inOrderTraversal(root->right, values);
        }
    }
    int kthSmallest(TreeNode* root, int k) {
        vector<int> values;
        inOrderTraversal(root, values);

        int smallest = values[k -1];
        return smallest;
    }
};