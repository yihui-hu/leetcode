class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_string = ""

        for char in s:
          if char.isalnum():
            processed_string += char.lower()
        
        start = 0
        end = len(processed_string) - 1

        while start <= end:
          if processed_string[start] != processed_string[end]:
            return False
          start += 1
          end -= 1
        
        return True