from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        prev = None
        head2 = None
        while curr is not None and curr.next is not None:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            if head2 is None:
                head2 = temp
            elif prev is not None:
                prev.next = temp
            prev = curr
            curr = curr.next
        return head2