class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        """
        similar to subset I
        perform brute-force backtracking with the choice to include
        or exclude the current number

        but since we have duplicates,
        everytime we branch out
        we want to skip over duplicate numbers in certain branches
        and so we have to sort nums first
        """

        def backtrack(i, subset):
          if i == len(nums):
            res.append(subset.copy())
            return
          
          # choice that includes nums[i]
          subset.append(nums[i])
          backtrack(i + 1, subset)

          # choice that excludes nums[i]
          subset.pop()
          while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
          backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res