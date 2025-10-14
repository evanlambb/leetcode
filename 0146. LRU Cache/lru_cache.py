class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.key = -1
        self.next = next
        self.prev = prev

## Head is the MRU 
## Tail is the LRU
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.dic = dict()
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity

    def get(self, key: int) -> int:
        # Check to see if it is in the dict...
        if key in self.dic:
            # update the node's position in the Llist
            n = self.dic[key] # This is the node that we now need to move

            n.prev.next = n.next
            n.next.prev = n.prev # Now the Node has been remove from the Llist

            n.next = self.head.next
            n.prev = self.head
            n.next.prev = n
            self.head.next = n

            # else, return the value of the node
            return self.dic[key].val

        # That node DNE, return -1
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.dic:
            # simply update the value...
            n = self.dic[key]
            n.val = value
            n.prev.next = n.next
            n.next.prev = n.prev
            n.next = self.head.next
            n.prev = self.head
            self.head.next.prev = n
            self.head.next = n

            return

        # We check if we are at capacity,
        elif self.size >= self.capacity and self.size != 0:
            # We remove the LRU
            lru = self.tail.prev
            del self.dic[lru.key]
            lru.prev.next = self.tail
            lru.next.prev = lru.prev
            self.size -= 1

        # We can safely just add
        n = Node(value)
        n.next = self.head.next
        n.prev = self.head
        n.next.prev = n
        n.key = key
        self.head.next = n
        self.size += 1
        self.dic[key] = n


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)