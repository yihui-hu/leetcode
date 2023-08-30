class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

      """
      naive solution, time limit exceeded
      """

      # if len(p) > len(s):
      #   return []

      # start, end = 0, len(p) - 1

      # charMap = {}

      # for char in p:
      #   if char in charMap:
      #     charMap[char] += 1
      #   else:
      #     charMap[char] = 1

      # res = []

      # while end < len(s):
      #   word = s[start:end + 1]

      #   valid = True
      #   charMap2 = {}
      #   for char in word:
      #     if char in charMap2:
      #       charMap2[char] += 1
      #     else:
      #       charMap2[char] = 1
          
      #   if charMap2 != charMap:
      #     valid = False

      #   if valid:
      #     res.append(start)
        
      #   start += 1
      #   end += 1

      #   refCharMap = charMap.copy()

      # return res

      """
      more optimized solution
      """

      if len(p) > len(s):
        return []

      sCount, pCount = {}, {}
      for i in range(len(p)):
        pCount[p[i]] = 1 + pCount.get(p[i], 0)
        sCount[s[i]] = 1 + sCount.get(s[i], 0)

      res = [0] if pCount == sCount else []

      # use left and right pointers to optimize addition of
      # chars in sliding window to the dictionary
      # "abcdefg" -> abc, bcd, cde
      # see how we only remove the first letter and add the last letter
      # to the dict; that's what we're doing in this loop
      left = 0
      for right in range(len(p), len(s)):
        # update dictionary
        sCount[s[right]] = 1 + sCount.get(s[right], 0)
        sCount[s[left]] -= 1

        # remove from dict if letter count is 0
        if sCount[s[left]] == 0:
          sCount.pop(s[left])

        left += 1
        if sCount == pCount:
          res.append(left)
      
      return res