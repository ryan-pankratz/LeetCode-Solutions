/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public bool IsValidBST(TreeNode root) {
        return isValidBSTHelper(root, null, null);
    }

    private bool isValidBSTHelper(TreeNode root, Nullable<int> largest_right, Nullable<int> smallest_left) {
        if (root == null || (root.left == null && root.right == null)) return true;
        else if (root.left != null && root.right == null) {
            if (smallest_left == null || smallest_left > root.val) {
                smallest_left = root.val;
            }

            if (!validateRoot(root.left, largest_right, smallest_left)) return false;
            return isValidBSTHelper(root.left, largest_right, smallest_left);
        }
        else if (root.right != null && root.left == null) {
            if (largest_right == null || largest_right < root.val) {
                largest_right = root.val;
            }

            if (!validateRoot(root.right, largest_right, smallest_left)) return false;
            return isValidBSTHelper(root.right, largest_right, smallest_left);
        }
        else {
            Nullable<int> temp_l = smallest_left;

            if (smallest_left == null || smallest_left > root.val) {
                smallest_left = root.val;
            }

            if (!validateRoot(root.left, largest_right, smallest_left)) return false;
            else if (!isValidBSTHelper(root.left, largest_right, smallest_left)) return false;

            if (largest_right == null || largest_right < root.val) {
                largest_right = root.val;
            }

            if (!validateRoot(root.right, largest_right, temp_l)) return false;
            return isValidBSTHelper(root.right, largest_right, temp_l);
        }
    }

    private bool validateRoot(TreeNode root, Nullable<int> largest_right, Nullable<int> smallest_left) {
        return (largest_right == null || largest_right < root.val) && (smallest_left == null || smallest_left > root.val);
    }
}