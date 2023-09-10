class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        use a map
        the key will be characters in the word
        the value will be the word(s) themselves
        then just join all the values in the map at the end
        """

        map = {}

        for word in strs:
          key = "".join(sorted(word)) # make sure to sort word
          if key in map:
            map[key].append(word)
          else:
            map[key] = [word]
          
        return map.values()