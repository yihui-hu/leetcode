class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        brute force is n^3, cheecking all possible subarrays
        for (i = 0 ... n - 1)
          for (j = i ... n - 1)
              for (k = i ... j)
                compute sum <-- O(n^3)
        another optimization:
        for (i = 0 ... n - 1)
          for (j = i ... n - 1)
              curSum + num[j] <-- no third for loop, so O(n^2)
        """

        """
        edge cases:
        1. array with only one item
        2. array of all negative integers except last elem which is 1
        """

        """
        sliding window esque approach
        whenever we reach a number that causes maxSum to go negative,
        we get rid of the entire subarray because we know it's not needed
        [-2,1,-3,4,-1,2,1,-5,4]
        here, we have -2 and 1. 
        on the second iteration, we have -2 + 1 = -1
        obviously to make it better we get rid of -2 so the new subarray is 1
        then we go to -3, and -3 + 1 = -2
        that's bad, so we also get rid of 1 and -3 when we reach 4
        then we get to -1, and 4 + (-1) = 3
        still ok, so we keep going
        3 + 2 = 5
        still ok, keep going
        5 + 1 = 6
        still ok
        6 - 5 = 1
        still ok, keep going
        1 + 4 = 5
        still ok,
        but we kept 6 as our maxSum, so that's what we return
        also, if we ever want to return indices, it's as easy as keeping two
        new variables, start and end, and we can update them super easily
        """

        # initialize maxSum to be first item in array
        maxSum = nums[0]
        currentSum = 0

        # one pass
        for n in nums:
          # means the previous number caused the currentSum to become negative
          # we don't want that, so we get rid of all the previous values
          # and reset currentSum to zero
          if currentSum < 0:
            currentSum = 0
          # add current number to currentSum (could be adding onto existing
          # subarray, or creating a new one if currentSum was < 0)
          currentSum += n
          # keep updating maxSum each time
          maxSum = max(maxSum, currentSum)

        # return maxSum
        return maxSum
