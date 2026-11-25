# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: ListNode | None):
        if not head or not head.next:
            return head
        prev = None
        curr = head
        nxt = head.next

        while nxt:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next
        curr.next = prev
        head = curr
        
        return head
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head

        slow = head 
        fast = head.next

        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow = slow.next

        h2 = slow.next
        slow.next = None

        h2 = self.reverse(h2)

        h1 = head
        while h1 and h2:
            temp = h1.next
            h1.next = h2
            temp2 = h2.next
            h2.next = temp

            h1 = temp
            h2 = temp2
        