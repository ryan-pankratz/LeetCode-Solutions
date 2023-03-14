from __future__ import annotations
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = 0
        lst = ListNode()
        first = lst
        while r != 0 or l1 is not None or l2 is not None:
            a = 0
            b = 0
            if l1 is not None:
                a = l1.val
            if l2 is not None:
                b = l2.val

            var = a + b + r
            if var >= 10:
                if var >= 20:
                    var -= 20
                else:
                    var -= 10

            lst.val = var
            r = (a + b + r) // 10

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            if r != 0 or l1 is not None or l2 is not None:
                lst.next = ListNode()
                lst = lst.next
        return first
