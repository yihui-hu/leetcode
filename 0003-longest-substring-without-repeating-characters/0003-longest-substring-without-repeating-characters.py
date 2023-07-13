class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        sliding window
        iterate through the string and add chars to a set
        when we find a duplicate, we update our left pointer
        and remove the letters from the set,
        update current length of longest substring
        then we continue
        """

        charSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
          # if current char is in charSet
          while s[r] in charSet:
            # remove char(s) from set
            charSet.remove(s[l])
            # move left pointer i.e. update sliding window
            l += 1
          # add current character
          charSet.add(s[r])
          # update our result i.e. longest substring thus far
          # instead of r - l + 1, could also use set.size()
          result = max(result, r - l + 1)

        return result
            