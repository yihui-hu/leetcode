class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """
        easy first check is length
        use hashmap (dict) to keep track of count of letters
        and iterate through the letters (keys) for each to
        make sure they have the same count
        O(n) or rather O(s + t), same for space complexity
        """

        if len(s) != len(t):
          return False
        
        count_s, count_t = {}, {}

        for i in range(len(s)):
          # very useful method with .get(key, initial_value)
          # if key doesn't exist, intialize with initial_value and add 1
          count_s[s[i]] = 1 + count_s.get(s[i], 0)
          count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        for c in count_s:
          # we use count_t.get(...) because 
          # c might not exist in count_t
          if count_s[c] != count_t.get(c, 0):
            return False
        
        return True

        """
        there's a one liner in python which basically does
        what we just did
        return Counter(s) == Counter(t)
        """

        """
        how can we solve this with O(1) memory?
        we sort the strings, then iterate through the strings!
        another one liner:
        return sorted(s) == sorted(t)
        
        but sorting takes more time, O(n log n) worst time
        """


