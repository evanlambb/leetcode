from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while l1 or l2:
            if head == None:
                head = ListNode()

            if l1 and l2:
                s = l1.val + l2.val
                tens = int(s / 10) 
                curr.val = s % 10

                l1 = l1.next
                l2 = l2.next

                if tens != 0:
                    if not l1:
                        l1 = ListNode(tens, None)
                    else:
                        l1.val += tens

                if l1 or l2:
                    curr.next = ListNode()
                    curr = curr.next

            elif l1:
                s = l1.val
                tens = int(s / 10) 
                curr.val = s % 10

                l1 = l1.next
                if tens != 0:
                    if not l1:
                        l1 = ListNode(tens, None)
                    else:
                        l1.val += tens
                
                if l1 or l2:
                    curr.next = ListNode()
                    curr = curr.next


            elif l2:
                s = l2.val
                tens = int(s / 10) 
                curr.val = s % 10

                l2 = l2.next
                if tens != 0:
                    if not l1:
                        l1 = ListNode(tens, None)
                    else:
                        l1.val += tens
                
                if l1 or l2:
                    curr.next = ListNode()
                    curr = curr.next

        return head