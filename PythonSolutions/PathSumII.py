from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret_val = []
        if root == None:
            return ret_val
        else:
            ret_val = self._pathSumHelper(root, targetSum, [])
            return ret_val

    def _pathSumHelper(self, root: Optional[TreeNode], targetSum: int, pathsList: List[int]) -> List[List[int]]:
        if root.val == targetSum and root.left == None and root.right == None:
            pathsList.append(root.val)
            return [pathsList]
        elif root.left == None and root.right == None:
            return []
        elif root.right == None:
            l = []
            pathsList.append(root.val)
            l.extend(self._pathSumHelper(root.left, targetSum - root.val, pathsList))
            return l
        elif root.left == None:
            l = []
            pathsList.append(root.val)
            l.extend(self._pathSumHelper(root.right, targetSum - root.val, pathsList))
            return l
        else:
            l = []
            pathsList.append(root.val)
            pathsList2 = pathsList.copy()
            l.extend(self._pathSumHelper(root.left, targetSum - root.val, pathsList))
            l.extend(self._pathSumHelper(root.right, targetSum - root.val, pathsList2))
            return l