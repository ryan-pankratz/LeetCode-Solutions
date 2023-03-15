import java.util.ArrayList;

//Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class PostOrderTraversal {
    public List<Integer> postorderTraversal(TreeNode root) {
        List return_val = new ArrayList<Integer>();
        if (root == null) {
            return return_val;
        }
        else if (this.isEmpty(root)) {
            return_val.add(root.val);
        }
        else if (root.left == null) {
            return_val.addAll(postorderTraversal(root.right));
            return_val.add(root.val);
        }
        else if (root.right == null) {
            return_val.addAll(postorderTraversal(root.left));
            return_val.add(root.val);
        }
        else {
            return_val.addAll(postorderTraversal(root.left));
            return_val.addAll(postorderTraversal(root.right));
            return_val.add(root.val);
        }
        return return_val;
    }

    private boolean isEmpty(TreeNode root) {
        return root.left == null && root.right == null;
    }
}