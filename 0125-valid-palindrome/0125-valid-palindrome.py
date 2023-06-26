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

        processedString = ""

        for char in s:
          # to check if it's alphanumeric, 
          # i.e. ignore whitespaces and special characters
          if char.isalnum():
            # .lower() to ignore cases
            processedString += char.lower()

        # [::-1] reverses a string, so just check for equality
        return processedString == processedString[::-1]
        