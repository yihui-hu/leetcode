class MyQueue(object):

    def __init__(self):

        """
        initialize two stacks
        s1 will act as our queue
        but s2 will help along the way
        """

        self.s1 = []
        self.s2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        # let's say we have s1 = [1, 2, 3] and s2 = []
        # and we want to add 4

        # move all items in s1 to s2 first
        while (self.s1):
          temp = self.s1.pop()
          self.s2.append(temp)

        # so now s1 = [] and s2 = [3, 2, 1]
        
        # add s1 effectively to the end/bottom of the queue
        self.s1.append(x)

        # s1 = [4] and s2 = [3, 2, 1]
        
        # add back all items
        while (self.s2):
          temp = self.s2.pop()
          self.s1.append(temp)

        # s1 = [4, 1, 2, 3] and s2 = []

    def pop(self):
        """
        :rtype: int
        """

        # remember: pop removes the *last* element of the list
        item = self.s1.pop()
        return item
        

    def peek(self):
        """
        :rtype: int
        """
        
        # return [-1] because the first item is at the last index
        return self.s1[-1]

    def empty(self):
        """
        :rtype: bool
        """

        return not self.s1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()