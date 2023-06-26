class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        (edge) cases:
        aaa
        aa
        empty string
        """

        # processedString = ""

        # for char in s:
        #   # to check if it's alphanumeric, 
        #   # i.e. ignore whitespaces and special characters
        #   if char.isalnum():
        #     # .lower() to ignore cases
        #     processedString += char.lower()

        # # [::-1] reverses a string, so just check for equality
        # return processedString == processedString[::-1]


        """
        how about we try solving this without using alnum or
        without using extra memory? use two finger algorithm, L and R
        from both ends, keep incrementing L and decrementing R until
        they're the same or L > R
        to avoid using alnum, use ASCII value
        it will still be a linear time algorithm
        """

        l, r = 0, len(s) - 1

        while l < r:
          # increment / decrement l and r while
          # they are NOT alphanumeric
          while l < r and not self.alphaNum(s[l]):
            l += 1
          while r > l and not self.alphaNum(s[r]):
            r -= 1

          # ok, both are alphanumeric, now
          # check if they are the same character
          if s[l].lower() != s[r].lower():
            return False

          # increment / decrement l and r after check(s)
          l, r = l + 1, r - 1
        
        return True


    # ord() gets the ascii value of characters
    # this is our own custom alphaNum func, 
    # highly customizable
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


        