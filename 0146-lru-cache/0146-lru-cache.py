class ListNode:
    def __init__(self, key = -1, val= -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:


    def __init__(self, capacity: int):
        self.mapp = {}
        self.cap = capacity
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def deleteNode(self, node):
        nextNode = node.next
        prevNode = node.prev 
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insertAfterHead(self, node):
        nextNode = self.head.next
        nextNode.prev = node
        self.head.next = node 
        node.next = nextNode
        node.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.mapp:
            return -1
        
        node = self.mapp[key]
        value = node.val

        self.deleteNode(node)
        self.insertAfterHead(node)

        return value
        
    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            node = self.mapp[key]
            node.val = value

            self.deleteNode(node)
            self.insertAfterHead(node)

            return 
        
        if len(self.mapp) == self.cap:
            node = self.tail.prev

            del self.mapp[node.key]
            self.deleteNode(node)
            
        newNode = ListNode(key, value)
        self.mapp[key] = newNode
        self.insertAfterHead(newNode)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)