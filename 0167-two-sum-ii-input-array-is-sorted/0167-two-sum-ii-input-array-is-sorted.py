class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        intuition: use binary search
        search from the middle:
          if smaller than target, vals are all on left of mid
          if larger than or equal to target, vals are all on right of mid

        another approach:
        use two pointers (one on each end)
        depending on sum of two pointers, move either left or right
        finish when l >= r (either found or not found)
        """

        l, r = 0, len(numbers) - 1

        while l < r:
          currSum = numbers[l] + numbers[r];
          if currSum < target:
            l += 1
          elif currSum > target:
            r -= 1
          else:
            return [l + 1, r + 1]
        
        return