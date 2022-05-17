class DoubleLinkedListNode:
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DoubleLinkedListNode()
        self.tail = DoubleLinkedListNode() # LRU

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def insert(self, node): # insert to head
        temp = self.head.next
        self.head.next = node
        node.next = temp

        temp.prev = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = DoubleLinkedListNode(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            node = self.tail.prev
            self.remove(node)
            del self.cache[node.key]