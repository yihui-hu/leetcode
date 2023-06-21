class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        naive solution: try all combinations, n^2
        """

        # left = buy index, right = sell index
        l, r = 0, 1
        max_profit = 0

        # iterate through entire prices array
        while r < len(prices):
          # if we have profit, calculate current profit and
          # check if it's lower than our current max profit
          if prices[l] < prices[r]:
            current_profit = prices[r] - prices[l]
            max_profit = max(max_profit, current_profit)
          else:
            # instead of moving by just one spot, move l to r because
            # we found a new lower price
            l = r
          # move right pointer regardless of condition
          r += 1
        
        return max_profit