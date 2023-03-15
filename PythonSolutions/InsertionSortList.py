# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def _helper(self, list):
        if list != []:
            self.val=list[0]
            curr = self
            for i in list[1:]:
                curr.next = ListNode(i)
                curr = curr.next

    def __str__(self):
        if self is None:
            return "None"
        return str(self.val) + " -> " + str(self.next)

    def __repr__(self):
        return self.__str__()

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        currentSortedIndex = 0
        currPrev = None
        while curr is not None:
            currNext = curr.next # To stop list from breaking
            curr2 = head
            prev = None
            for _ in range(currentSortedIndex + 1):
                if curr2 is None or curr.val < curr2.val:
                    # Insert Here:
                    curr.next = curr2
                    if prev is not None:
                        prev.next = curr
                    if currPrev is not None:
                        currPrev.next = currNext
                else:
                    prev = curr2
                    curr2 = curr2.next
            curr = currNext
            currentSortedIndex += 1
        return head

if __name__ == '__main__':
    a = ListNode()
    a._helper([4,2,1,3])
    s = Solution()
    s.insertionSortList(a)
    print(a)
