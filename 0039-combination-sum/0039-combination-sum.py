class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

      """
      use a decision tree of sorts
      for each node, we make the decision to include or exclude the current
      elem candidates

      time complexity is O(2^target)
      """

      res = []

      # i = maintains which of the candidate we include
      # curr = tells us what we've added to the current comb so far
      # total = total sum of elems in curr
      def dfs(i, curr, total):
        # base case
        if total == target:
          res.append(curr.copy()) # add combination to the res array
          return

        if i >= len(candidates) or total > target:
          return

        # here, we run the two branch decision DFS 

        # first decision where we include the candidate
        curr.append(candidates[i])
        dfs(i, curr, total + candidates[i])

        curr.pop() # remove the last decision we made

        # second decision where we exclude the candidate
        dfs(i + 1, curr, total) 

      dfs(0, [], 0)
      return res