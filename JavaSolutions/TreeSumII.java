import java.util.ArrayList;


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
class TreeSumII {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            List<List<Integer>> ret = new ArrayList<>();
            return ret;
        }
        else {
            ArrayList<Integer> al = new ArrayList<>();
            return pathSumHelper(root, targetSum, al);
        }
    }

    private List<List<Integer>> pathSumHelper(TreeNode root, int targetSum, List<Integer> pathsList) {
        ArrayList<List<Integer>> ret_val = new ArrayList<>();
        if (root.val == targetSum && root.left == null && root.right == null) {
            pathsList.add(root.val);
            ret_val.add(pathsList);
            return ret_val;
        }
        else if (root.left == null && root.right == null)
            return ret_val;
        else if (root.right == null) {
            pathsList.add(root.val);
            ret_val.addAll(pathSumHelper(root.left, targetSum - root.val, pathsList));
            return ret_val;
        }
        else if (root.left == null) {
            pathsList.add(root.val);
            ret_val.addAll(pathSumHelper(root.right, targetSum - root.val, pathsList));
            return ret_val;
        }
        else {
            pathsList.add(root.val);
            ArrayList<Integer> pathsListTwo =  new ArrayList<>(pathsList);
            ret_val.addAll(pathSumHelper(root.left, targetSum - root.val, pathsList));
            ret_val.addAll(pathSumHelper(root.right, targetSum - root.val, pathsListTwo));
            return ret_val;
        }

    }
}