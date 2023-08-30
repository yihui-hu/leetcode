class Solution:
    def myAtoi(self, s: str) -> int:
      """
      first, trim the string to remove any leading / trailing whitespace
      check first char: 
        positive = true
        if it's '-':
          positive = false
        elif '+':
          continue
      """

      """
      edge cases:
      "    +2345" ?
      "   -   4563" ?
      """

      s = s.strip(' ')

      if len(s) == 0:
        return 0

      positive = True
      digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
      startedNum = False
      index = 0

      while index < len(s) and s[index] == ' ':
        index += 1

      if s[index] == '-':
        positive = False
        index += 1
      elif s[index] == '+':
        index += 1

      num = ''
      while index < len(s) and s[index] in digits:
        num += s[index]
        index += 1

      if num != '':
        num = int(num)

        if not positive:
          num *= -1 

        if num > (2 ** 31 - 1):
          num = 2 ** 31 - 1
        elif num < -(2 ** 31):
          num = -(2 ** 31)

        return num
      else:
        return 0

