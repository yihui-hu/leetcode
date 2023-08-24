class Solution:
    def addBinary(self, a: str, b: str) -> str:
      # convert binaries to integers
      intA = int(a, 2) # 2 as base because binary
      intB = int(b, 2) 

      intSum = intA + intB

      return bin(intSum)[2:] # convert back to binary