struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {return nullptr;}
        if (head->next == nullptr) {return head;}
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* nxt = head->next;

        while (nxt) {
            curr->next = prev; 
            prev = curr;
            curr = nxt;
            nxt = nxt->next;
        }
        curr->next = prev;
        return curr;
    }

    ListNode* mergeLists(ListNode* l1, ListNode* l2) {
        // alternate between l1 and l2 until one of them is empty... 
        ListNode* head = l1;
        // either l1 and l2 are hte same length or l1 is 1 longer
        while (l1 && l2) {
                ListNode* temp = l1->next;
                l1->next = l2;
                ListNode* temp2 = l2->next;
                l2->next = temp;
                l2 = temp2;
                l1 = temp;
        } 
        return head;
    }

    void reorderList(ListNode* head) {
        // we are going to perform the following:
        // 1. find the middle
        // 2. reverse the second half
        // 3. merge the two half lists
        // 4. save the final in head

        // 1.
        ListNode* mid = head;
        ListNode* end = head;
        while (end) {
            end = end->next;
            if (end) {end = end->next;}
            if (!end) {
                ListNode* temp = mid;
                mid = mid->next;
                temp->next = nullptr;
            }  else {mid = mid->next;}
        }
        // 2.
        mid = reverseList(mid);

        // 3. 
        head = mergeLists(head, mid);
    }
};