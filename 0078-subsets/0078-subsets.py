class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        subset = []

        def dfs(index):
          if index >= len(nums):
            result.append(list(subset))
            return
          
          # decision to include current num in subset
          subset.append(nums[index])
          dfs(index + 1)

          # decision to exclude current num in subset
          subset.pop()
          dfs(index + 1)
        
        dfs(0)
        return result