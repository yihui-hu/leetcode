class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        """
        get two stacks,
        one to hold the tokens
        and another to hold current operation
        """

        stack = [] # can use normal list as stack, just append() and pop()
        for exp in tokens:
          if exp == '+':
            stack.append(stack.pop() + stack.pop())
          elif exp == '-':
            # order matters, so need to do this 
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 - num2)
          elif exp == '/':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(int(float(num1)/num2))
          elif exp == '*':
            stack.append(stack.pop() * stack.pop())
          else:
            stack.append(int(exp))
          
        return stack.pop()
