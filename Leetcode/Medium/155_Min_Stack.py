class MinStack:
    """Create the stack that can get the minimum value in O(1) time.
    """
    def __init__(self):
        self._stack = [] # use array to implement our stack
        self._min_stack = [] # use another stack to store the Current Minimum Value at Each Layer of the stack

    def push(self, val: int) -> None:
        self._stack.append(val) # push the value into the stack
        cur_min_stack = min(val, self._min_stack[-1] if self._min_stack else val) # get the current minimum value at this layer
        self._min_stack.append(cur_min_stack) # push the current minimum value into the min_stack

    def pop(self) -> None:
        self._stack.pop() # pop the value from the stack
        self._min_stack.pop() # pop the current minimum value from the min_stack

    def top(self) -> int:
        return self._stack[-1] # get the top value from the stack

    def getMin(self) -> int:
        return self._min_stack[-1] # get the current minimum value from the min_stack
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()