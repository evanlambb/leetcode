/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
    unordered_map<Node*, Node*> seen; // <node address in oringinal list -> node address in new list>
public:
    Node* copyRandomList(Node* head) {
        if (!head) {return nullptr;}
        cout << head->val << endl;
        if (seen.find(head) != seen.end()) {return seen[head];}

        // we need a new node here
        Node* n = new Node(head->val);
        seen[head] = n;
        n->random = seen.find(head->random) != seen.end() ? seen[head->random] : copyRandomList(head->random);
        n->next = copyRandomList(head->next);
        // add the node to the map
        return n;
    }
};