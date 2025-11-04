from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists

        return lists[0]


    
    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 or l2:
            tail.next = ListNode()
            tail = tail.next
            if l1 and l2:
                if l1.val <= l2.val:
                    tail.val = l1.val
                    l1 = l1.next
                else:
                    tail.val = l2.val
                    l2 = l2.next
            elif l1:
                tail.val = l1.val
                l1 = l1.next
            else:
                tail.val = l2.val
                l2 = l2.next

        return dummy.next