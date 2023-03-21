from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidHelper(root, None, None)

    def _isValidHelper(self, root: Optional[TreeNode], largest_right: Optional[int], smallest_left: Optional[int]):
        if root is None or (root.left is None and root.right is None):
            return True
        elif root.left is not None and root.right is None:
            if smallest_left is None or smallest_left > root.val:
                smallest_left = root.val
            if not self._validate_root(root.left, largest_right, smallest_left):
                return False
            return self._isValidHelper(root.left, largest_right, smallest_left)
        elif root.right is not None and root.left is None:
            if largest_right is None or largest_right < root.val:
                largest_right = root.val
            if not self._validate_root(root.right, largest_right, smallest_left):
                return False
            return self._isValidHelper(root.right, largest_right, smallest_left)
        else:
            temp_l = smallest_left

            if smallest_left is None or smallest_left > root.val:
                smallest_left = root.val
            if not self._validate_root(root.left, largest_right, smallest_left):
                return False
            elif not self._isValidHelper(root.left, largest_right, smallest_left):
                return False

            if largest_right is None or largest_right < root.val:
                largest_right = root.val
            if not self._validate_root(root.right, largest_right, temp_l):
                return False
            return self._isValidHelper(root.right, largest_right, temp_l)

    def _validate_root(self, root: TreeNode, largest_right: Optional[int], smallest_left: Optional[int]):
        return (largest_right is None or root.val > largest_right) and (
                    smallest_left is None or root.val < smallest_left)
