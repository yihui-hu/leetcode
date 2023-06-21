class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        1. use stack lol
        2. create dictionary of valid brackets
        """

        closing_brackets = {
          ')' : '(',
          ']' : '[',
          '}' : '{'
        }

        stack = []
        # enumerate over brackets
        for index, char in enumerate(s):
          # if char is closing bracket, check stack
          if char in closing_brackets:
            if stack and closing_brackets[char] == stack[-1]:
              stack.pop()
            else:
              return False
          # else, add char to stack
          else:
            stack.append(char)
        
        # if stack is empty
        if not stack:
          return True
        # if stack still has leftover bracket(s)
        else:
          return False



