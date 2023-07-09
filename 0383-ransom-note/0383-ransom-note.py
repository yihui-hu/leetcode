class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        """
        use a dictionary
        and then decrement
        """

        magazine_letters = {}
        for letter in magazine:
          magazine_letters[letter] = 1 + magazine_letters.get(letter, 0)
        
        for letter in ransomNote:
          if magazine_letters.get(letter, 0 ) == 0:
            return False
          else:
            magazine_letters[letter] -= 1

        return True