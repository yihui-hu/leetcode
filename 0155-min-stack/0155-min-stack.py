class MinStack(object):

    def __init__(self):
        # define two stacks: one to hold actual nodes
        # and another to hold the min element at that pos

        """
        we need to keep a minStack and keep adding to it
        because when we pop items off the stack, the minimum
        in the stack might change and we don't have that prev 
        elem saved.

        overview (left is top):
        stack = []

        add 1 to stack
        stack = [1]
        minStack = [1]

        add -2 to stack
        stack = [-2, 1]
        minStack = [-2, 1]

        add 1 to stack
        stack = [1, -2, 1]
        minStack = [-2, -2, 1]
        """
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        # here we are adding the current min elem of the stack to minStack
        val = min(val, self.minStack[-1] if self.minStack else val) # need the if in case minStack is empty
        self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()