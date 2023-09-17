class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        honestly kind of mind-melting
        but neetcode cleared it up a bit
        hot take: he doesn't explain things very well sometimes,
        i understand why it works
        but not how
        how can it be guaranteed that this finds all subarrays?
        https://www.youtube.com/watch?v=fFVZt-6sgyo
        """

        """
        in any case, this is O(n) time and space complexity
        """

        res = 0
        currSum = 0
        prefixSums = {0 : 1} # the empty subarray, edge / base case

        for num in nums:
          currSum += num
          diff = currSum - k

          # check to see if the difference exists in the hashmap:
          # that means we can exclude some prefixes to make currSum match k
          # and thus we add those ways to our results
          res += prefixSums.get(diff, 0)

          # add prefix sum to hashmap
          prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        
        return res
          



