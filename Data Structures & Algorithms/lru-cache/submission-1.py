class Node:
    def __init__(self, key: int, value:int):
        self.key = key
        self.value = value
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.right = self.right
        self.right.left = self.left
        self.capacity = capacity
        self.size = 0
    
    def remove(self, node: Node):
        prev, nxt = node.left, node.right
        if prev:
            prev.right = nxt
        if nxt:
            nxt.left = prev
    
    def add(self, node):
        prev = self.right.left
        node.right = self.right
        node.left = prev
        self.right.left = node
        if prev:
            prev.right = node


    def get(self, key: int) -> int:
        node = self.hashmap.get(key, -1)
        if node == -1:
            return -1
        else:
            self.remove(node)
            self.add(node)
            return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.remove(self.hashmap[key])
            self.add(self.hashmap[key])
            return
        else:
            node = Node(key, value)
            self.add(node)
            self.hashmap[key] = node
            self.size += 1
            if self.size > self.capacity:
                node = self.left.right
                del self.hashmap[node.key]
                self.remove(node)
                self.size -= 1

