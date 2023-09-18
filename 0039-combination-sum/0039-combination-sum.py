class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

      """
      use a decision tree of sorts
      for each node, we make the decision to include or exclude the current
      elem candidates, in order to get all unique combinations

      time complexity is O(2^target)
      """

      res = []

      def dfs(index, candidate):
        if sum(candidate) == target:
          res.append(candidate.copy())
          return
        
        if index >= len(candidates) or sum(candidate) > target:
          return
        
        # now we make choices

        candidate.append(candidates[index])
        dfs(index, candidate)

        candidate.pop()
        dfs(index + 1, candidate)
      
      dfs(0, [])
      return res

      res = []

      # # i = maintains which of the candidate we include
      # # curr = tells us what we've added to the current comb so far
      # # total = total sum of elems in curr
      # def dfs(i, curr, total):
      #   # base case
      #   if total == target:
      #     res.append(curr.copy()) # add combination to the res array
      #     return

      #   if i >= len(candidates) or total > target:
      #     return

      #   # first decision where we include the candidate
      #   curr.append(candidates[i])
      #   dfs(i, curr, total + candidates[i])

      #   # second decision where we exclude the candidate
      #   curr.pop()
      #   dfs(i + 1, curr, total) 

      # dfs(0, [], 0)
      # return res