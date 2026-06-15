# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast pointer slow pointer
        slow, fast = head, head.next
        if head.next == None:
            return None

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        slow.next = slow.next.next
        return head