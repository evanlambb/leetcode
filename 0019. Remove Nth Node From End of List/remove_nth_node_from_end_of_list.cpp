struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}     ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr) {return nullptr;}
        ListNode* it = head;
        ListNode* start = head;
        int count = 0;
        while (count < n) {
            if (it == nullptr) {return head->next;}
            it = it->next;
            count += 1;
        } 
        if (it == nullptr) {return head->next;}
        while (it->next != nullptr) {
            it = it->next;
            start = start->next;
        }
       
       // remove the next
        ListNode* del = start->next;
        start->next = del->next;
        del->next = nullptr; // I may need to manually delete here if not RAII
        return head;
    }
};