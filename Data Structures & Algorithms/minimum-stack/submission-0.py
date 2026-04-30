class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack  or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if tmp == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
