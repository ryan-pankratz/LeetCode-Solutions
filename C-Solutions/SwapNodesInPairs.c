/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head){
    if (head == NULL || head->next == NULL) return head;

    struct ListNode* curr = head;
    struct ListNode* prev = NULL;
    struct ListNode* head2 = NULL;

    while (curr != NULL && curr->next != NULL) {
        struct ListNode* temp = curr->next;
        curr->next = temp->next;
        temp->next = curr;
        if (head2 == NULL)
            head2 = temp;
        else if (prev != NULL)
            prev->next = temp;
        
        prev = curr;
        curr = curr->next;
    }
    return head2;
}