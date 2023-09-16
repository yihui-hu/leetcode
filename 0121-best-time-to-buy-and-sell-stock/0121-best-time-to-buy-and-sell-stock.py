class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        
        max_profit = 0
        while right < len(prices):
          # calculate curr profit, check if it's > curr max profit
          if prices[left] < prices[right]:
            max_profit = max(max_profit, prices[right] - prices[left])
          else:
            # we found a new minimum at r, so we move l to r
            left = right
          # always increment r
          right += 1
        
        return max_profit