// Definition for singly-linked list.
 public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }

class InsertionSortList {
    public ListNode insertionSortList(ListNode head) {
        if (head == null)
            return head;

        ListNode curr = head;
        int currentSortedIndex = 0;
        while (curr.next != null) {
            ListNode currNext = curr.next.next;
            ListNode nodeTemp = curr.next;
            ListNode curr2 = head;
            curr.next = currNext;
            ListNode prev = null;
            boolean uninserted = true;

            for (int i = 0; i < currentSortedIndex + 1; i++) {
                if (curr2 == null || nodeTemp.val < curr2.val) {
                    nodeTemp.next = curr2;
                    if (prev != null)
                        prev.next = nodeTemp;
                    else if (i == 0)
                        head = nodeTemp;
                    uninserted = false;
                    break;
                }
                else {
                    prev = curr2;
                    curr2 = curr2.next;
                }
            }
            if (uninserted) {
                curr.next = nodeTemp;
                curr = curr.next;
            }
            currentSortedIndex += 1;
        }
        return head;
    }
}