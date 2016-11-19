/*
143. Reorder List 
 Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}. 

解题思路：

先把链表分开成两个部分，前一半后一半

然后把后半个reverse，用前后指针可以完成这个功能

在遍历两个链表就可以了

*/
void reorderList(struct ListNode* head) {
    struct ListNode *fast = head, *slow = head, *tmp, *tmp_head = NULL, *tmp_tail;
    
    while(NULL != fast&&NULL != fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }
    if(NULL == fast){
        tmp_tail = slow;
    }
    else{
        tmp_tail = slow->next;
    }
    while(NULL != tmp_tail){
            tmp = tmp_tail->next;
            tmp_tail->next = tmp_head;
            tmp_head = tmp_tail;
            tmp_tail = tmp;
    }
    slow = tmp_head;
    if(NULL == fast){
        while(NULL != slow){
            tmp = slow->next;
            slow->next = head->next;
            if(NULL == tmp){
                slow->next = NULL;
            }
            head->next = slow;
            head = slow->next;
            slow = tmp;
        }
    }
    else{
        while(NULL != slow){
            tmp = slow->next;
            slow->next = head->next;
            head->next = slow;
            head = slow->next;
            slow = tmp;
        }
        head->next = NULL;
    }
}
