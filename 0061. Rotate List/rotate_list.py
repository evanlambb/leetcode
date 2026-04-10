# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getLength(node: Optional[ListNode]) -> int:
            return 1 + getLength(node.next) if node else 0
        l = getLength(head)
        if l == 0:
            return head
        k %= l 
       
        node = head
        for _ in range(l - k - 1):
            node = node.next


        end = node

        while end.next:
            end = end.next

        end.next = head
        head = node.next
        node.next = None
        return head