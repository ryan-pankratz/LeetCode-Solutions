from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        elif root.left == None:
            l = []
            l.extend(self.postorderTraversal(root.right))
            l.append(root.val)
            return l
        elif root.right == None:
            l = []
            l.extend(self.postorderTraversal(root.left))
            l.append(root.val)
            return l
        else:
            l = []
            l.extend(self.postorderTraversal(root.left))
            l.extend(self.postorderTraversal(root.right))
            l.append(root.val)
            return l