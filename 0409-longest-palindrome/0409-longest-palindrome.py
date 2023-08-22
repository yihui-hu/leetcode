class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        create hash map
        if key has odd number of vals:
          update maxOdd
        if key has even number of vals:
          add to running length        
        """

        # map = {}

        # for c in range(len(s)):
        #   if map[c]:
        #     map[c] += 1
        #   else:
        #     map[c] = 1

        odd = 0
        length = 0

        # collections.Counter([], string, etc.)
        # counts the number of occurences of 'elems' in the object
        # and here we iterate through the values
        # because the actual keys themselves don't matter
        for count in collections.Counter(s).values():
          # if char has even num of chars
          if count % 2 == 0:
            length += count
          # char has odd num of chars
          else:
            odd = 1
            length += count - 1 # use an even num of the odd count

        # we add ans and odd, which will always be 1,
        # because we can add char in the middle
        return length + odd 

