class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        """
        cannot do greedy approach
        since we want the *fewest* amount of coins
        also, can't do DFS and backtracking using a decision tree
        since the time complexity will be super long
        
        DP bottom up approach (similar to climbing stairs)
        DP = []
        coins = [1, 3, 4, 5], target = 7
        how many coins do we use to get value of 0? 0, so DP[0] = 0
        value of 1? DP[1] = 1 (bc 1 exists)
        value of 2? 1 + DP[2 - 1] = 1 + DP[1] = 2
        value of 3? 1 + DP[2] = 2 or 1 (bc 3 exists)
        value of 4? 1 + DP[3] = 2 or 1 + DP[1] = 2
        value of 5? 1 + DP[4] = 3 or 1 + DP[2] = 3 or 1 (bc 5 exists)
        """
        
        # initialize dp array of amount + 1 since we want to
        # compute 0 ... amount
        # default value to give will be amount + 1, just a max val of sorts
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for amt in range(1, amount + 1):
            for c in coins:
                # get the remaining amt   
                if amt - c >= 0:
                    # the 1 comes from the coin that we're using
                    dp[amt] = min(dp[amt], 1 + dp[amt - c])
                
                """
                basically, if
                coin = 4
                amt = 7
                dp[7] = min(dp[7], 1 + dp[3])
                """
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
        """
        time complexity is O(amount * len(coins)), so O(n^2) if both are close
        space complexity is O(amount)
        """