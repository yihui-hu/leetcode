class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

      """
      bottom up DP approach
      https://www.youtube.com/watch?v=Sx9NNgInc3A
      """

      dp = [False] * (len(s) + 1)

      # we set last index to true because if we ever reach it,
      # that means we could successfully match the entire word
      dp[len(s)] = True 

      # start from the bottom
      for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
          if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
            dp[i] = dp[i + len(w)]
          if dp[i] == True:
            break
      
      return dp[0]