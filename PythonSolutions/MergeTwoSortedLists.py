# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        else:
            lst = ListNode()
            curr1 = list1
            curr2 = list2
            curr_node = lst
            while curr1 is not None or curr2 is not None:
                if curr1 is None:
                    curr_node.val = curr2.val
                    curr2 = curr2.next
                elif curr2 is None:
                    curr_node.val = curr1.val
                    curr1 = curr1.next
                elif curr1.val <= curr2.val:
                    curr_node.val = curr1.val
                    curr1 = curr1.next
                else:
                    curr_node.val = curr2.val
                    curr2 = curr2.next

                if curr1 is not None or curr2 is not None:
                    curr_node.next = ListNode()
                    curr_node = curr_node.next

        return lst