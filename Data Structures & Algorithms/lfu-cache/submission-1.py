from collections import defaultdict

class Node:
    def __init__(self, key=0, value=0) -> None:
        self.key = key
        self.value = value
        self.left, self.right = None, None
        self.freq = 1

class LinkedList:
    def __init__(self) -> None:
        self.start, self.end = Node(0,0), Node(0,0)
        self.start.right = self.end
        self.end.left = self.start
        self.length = 0

    def remove(self, Node):
        prev, nxt = Node.left, Node.right
        prev.right, nxt.left = nxt, prev
        self.length -= 1
    
    def add(self, node):
        prev = self.end.left
        prev.right = node
        node.left = prev
        node.right = self.end
        self.end.left = node
        self.length += 1


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodemap = {}
        self.listmap = defaultdict(LinkedList)
        self.minfreq = 1

    def useCounter(self, node: Node):
        prevlist = self.listmap[node.freq]
        if prevlist.length == 1 and node.freq == self.minfreq:
            self.minfreq += 1
        prevlist.remove(node)
        node.freq += 1
        self.listmap[node.freq].add(node)
        


    def get(self, key: int) -> int:
        if key in self.nodemap:
            node = self.nodemap[key]
            self.useCounter(node)
            return node.value
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodemap:
            node = self.nodemap[key]
            self.useCounter(node)
            node.value = value
            return
        

        if len(self.nodemap) == self.capacity:
            targetlist = self.listmap[self.minfreq]
            node = targetlist.start.right
            del self.nodemap[node.key]
            targetlist.remove(node)
        
        node = Node(key,value)
        self.nodemap[key] = node
        self.listmap[1].add(node)
        self.minfreq = 1

        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)