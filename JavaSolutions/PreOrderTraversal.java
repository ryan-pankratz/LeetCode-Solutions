import java.util.ArrayList;

// Definition for a binary tree node.
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

class PreOrderTraversal {
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> ret_val = new ArrayList<>();
        if (root == null)
            return ret_val;
        ret_val.add(root.val);
        ret_val.addAll(preorderTraversal(root.left));
        ret_val.addAll(preorderTraversal(root.right));
        return ret_val;
    }
}