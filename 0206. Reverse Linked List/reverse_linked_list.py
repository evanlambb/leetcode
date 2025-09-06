from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n1 = None
        n2 = head
        if head == None:
            return None
        
        n3 = n2
        while not n3 == None:
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        return n1