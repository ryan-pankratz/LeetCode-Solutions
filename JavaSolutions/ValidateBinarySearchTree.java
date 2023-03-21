import java.lang.Integer;

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
class ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        return isValidBSTHelper(root, null, null);
    }

    private boolean isValidBSTHelper(TreeNode root, Integer largest_right, Integer smallest_left) {
        if (root == null || (root.left == null && root.right == null)) return true;
        else if (root.left != null && root.right == null) {
            if (smallest_left == null || smallest_left.intValue() > root.val) {
                smallest_left = Integer.valueOf(root.val);
            }

            if (!validateRoot(root.left, largest_right, smallest_left)) return false;
            return isValidBSTHelper(root.left, largest_right, smallest_left);
        }
        else if (root.right != null && root.left == null) {
            if (largest_right == null || largest_right.intValue() < root.val) {
                largest_right = Integer.valueOf(root.val);
            }

            if (!validateRoot(root.right, largest_right, smallest_left)) return false;
            return isValidBSTHelper(root.right, largest_right, smallest_left);
        }
        else {
            Integer temp_l = smallest_left;

            if (smallest_left == null || smallest_left.intValue() > root.val) {
                smallest_left = Integer.valueOf(root.val);
            }

            if (!validateRoot(root.left, largest_right, smallest_left)) return false;
            else if (!isValidBSTHelper(root.left, largest_right, smallest_left)) return false;

            if (largest_right == null || largest_right.intValue() < root.val) {
                largest_right = Integer.valueOf(root.val);
            }

            if (!validateRoot(root.right, largest_right, temp_l)) return false;
            return isValidBSTHelper(root.right, largest_right, temp_l);
        }
    }

    private boolean validateRoot(TreeNode root, Integer largest_right, Integer smallest_left) {
        return (largest_right == null || largest_right.intValue() < root.val) && (smallest_left == null || smallest_left.intValue() > root.val);
    }
}
