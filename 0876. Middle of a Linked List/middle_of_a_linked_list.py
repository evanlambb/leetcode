from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        mid = head
        if not head.next:
            return head
        while head.next:
            if count == 0:
                mid = mid.next
                count += 1
            elif count >= 1:
                count = 0
            
            head = head.next


        return mid
        