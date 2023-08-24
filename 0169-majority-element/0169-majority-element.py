class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      dict = {}

      for num in nums:
        if num in dict:
          dict[num] += 1
        else:
          dict[num] = 1
        
        if dict[num] > len(nums)//2:
          return num