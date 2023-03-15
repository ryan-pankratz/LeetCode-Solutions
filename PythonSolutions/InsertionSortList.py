# Definition for singly-linked list.
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        curr = head
        currentSortedIndex = 0
        while curr.next is not None:
            currNext = curr.next.next # To stop list from breaking
            nodeTemp = curr.next
            curr2 = head
            prev = None
            curr.next = currNext
            uninserted = True
            for i in range(currentSortedIndex + 1):
                if curr2 is None or nodeTemp.val < curr2.val:
                    # Insert Here:
                    nodeTemp.next = curr2
                    if prev is not None:
                        prev.next = nodeTemp
                    elif i == 0:
                        head = nodeTemp
                    uninserted = False
                    break
                else:
                    prev = curr2
                    curr2 = curr2.next
            if uninserted:
                curr.next = nodeTemp
                curr = curr.next
            currentSortedIndex += 1
        return head
