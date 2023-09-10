class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        imagine a tree and perform DFS
        for each number in nums, we make a decision to either include or exclude it from the eventual unique subset
        """
        result = []

        subset = []
        def dfs(index):
          if (index >= len(nums)):
            # we've DFSed all the way to the bottom leaf
            # append the unique subset to our array
            result.append(list(subset))
            return

          # 1. decision to INCLUDE current number in subset
          subset.append(nums[index])
          dfs(index + 1)

          # 2. decision to EXCLUDE current number in subset
          subset.pop()
          dfs(index + 1)
        
        dfs(0)
        return result

        