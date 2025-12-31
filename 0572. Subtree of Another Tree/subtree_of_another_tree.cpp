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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) {return true;}
        if (!p || !q) {return false;}
        return p->val == q->val ? isSameTree(p->left, q->left) && isSameTree(p->right, q->right) : false;
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // try and find the subRoot, if it does not exist, return false, if it exists, return isSameTree...
        if (!subRoot) {return true;} // empty subRoot
        if (!root) {return false;} // it does not exist
        if (root->val == subRoot->val && isSameTree(root, subRoot) == true) {return true;}
        return isSubtree(root->left, subRoot) ||  isSubtree(root->right, subRoot);
    }
};