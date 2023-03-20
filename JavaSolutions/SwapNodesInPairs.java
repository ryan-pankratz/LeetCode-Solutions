/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class SwapNodesInPairs {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode curr = head;
        ListNode prev = null;
        ListNode head2 = null;

        while (curr != null && curr.next != null) {
            ListNode temp = curr.next;
            curr.next = temp.next;
            temp.next = curr;
            if (head2 == null)
                head2 = temp;
            else if (prev != null)
                prev.next = temp;

            prev = curr;
            curr = curr.next;
        }
        return head2;
    }
}