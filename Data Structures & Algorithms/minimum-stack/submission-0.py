class MinStack:

    def __init__(self):
        # what we basically do here is separate stacks for min and normal orders
        # the normal stack is just normal
        # the min stack is the minimum between the current min and whatever is getting added
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(self.minstack[-1], val))
        else:
            self.minstack.append(val)
        
    def pop(self) -> None:
        self.minstack.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
