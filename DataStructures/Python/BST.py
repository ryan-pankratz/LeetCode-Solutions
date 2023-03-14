from __future__ import annotations
from typing import Optional, Any

class BSTNode:
    """
    A node for a BST. Has an item and key attribute. Also has a count attribute for duplicate items.
    """
    item: Any
    key: int
    count: int

    def __init__(self, item: Any, key: int, right: Optional[BSTNode], left: Optional[BSTNode]) -> None:
        """
        Initializes the BST node.
        :param item: 
        :param key:
        """
        self.item = item
        self.key = key
        self.count = 1
        self.left = left
        self.right = right

