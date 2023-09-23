class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      
      """
      perform backtracking
      """

      result = []

      # base case
      if (len(nums) == 1):
        return [nums[:]]
      
      for i in range(len(nums)):
        # pop first value off and get permutations of the other vals
        n = nums.pop(0)
        perms = self.permute(nums)

        for perm in perms:
          perm.append(n)
        result.extend(perms)
        nums.append(n)

      # testing leethub
      return result



