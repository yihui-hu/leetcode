class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        """
        using dynamic programming, starting from the back (kind of like DFS)
        with a decision tree,
        you'll notice that you're doing a lot of repeat work
        and the same subproblems
        
        so do DP and work backward
        
        let's say you have 3 steps
        [1, 2, 3]
        
        ways to get to step 3 from step 3? 1 way 
        ways to get to step 3 from step 2? 1 way (1 step) + 1 way (prev comp)
        ways to get to step 3 from step 1? 
            you can take 1 step to get to step 2, and we know it takes 2 steps
            to get to step 3 from step 2
            OR you can take 2 steps to get to step 3, and we know it takes 1 step
            to get to step 3 from step 3
            SO in total, 2 way + 1 way = 3 ways
        """
        
        # this is a shortcut fibonacci sequence-like solution
        # let's say climbing stairs you can take 3 steps:
        # then, you would have one, two and three as variables
        # and add those
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one

        """
        fibonacci optimization (fast, but not the most memory efficient):
        store a list of fib numbers
        
        def fib_to(n):
            fibs = [0, 1]
            for i in range(2, n+1):
                fibs.append(fibs[-1] + fibs[-2]) # add the last two vals of the arr
                return fibs
        
        fib_to(n - 1)
        """