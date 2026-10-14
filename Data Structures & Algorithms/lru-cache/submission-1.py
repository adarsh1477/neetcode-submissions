class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left,self.right = Node(None,None),Node(None,None)
        self.cap = capacity
        self.left.next,self.right.prev = self.right,self.left
        self.cache = {}
        
    def insert(self,node):
        nxt = self.right
        prv = self.right.prev
        prv.next = nxt.prev = node
        node.next,node.prev = nxt,prv

    def remove(self,node):
        nxt,prv = node.next,node.prev
        nxt.prev,prv.next = prv,nxt        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]