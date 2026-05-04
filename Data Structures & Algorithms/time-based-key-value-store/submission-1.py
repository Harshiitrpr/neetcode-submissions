from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        self.hashmap = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(timestamp)
        self.hashmap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.keys[key])
        l, r = 0, n
        while l < r:
            m = l + (r - l)//2
            if self.keys[key][m] == timestamp:
                return self.hashmap[key][timestamp]
            elif self.keys[key][m] > timestamp:
                r = m
            else:
                l = m + 1
        if l == 0:
            return ""
        return self.hashmap[key][self.keys[key][l-1]]
        
