# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        lst = []
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        curr = head
        count = len(lst) - 1
        while curr is not None:
            if curr.val != lst[count]:
                return False
            count -= 1
            curr = curr.next
        return True
