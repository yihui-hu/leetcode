class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        """
        overview:
        set up prefix and postfix array
        
        so let's say you have
        nums = [1, 2, 3, 4]
        
        then your prefix arr is:
        prefix = [1, 2, 6, 24]
        (you basically multiply everything one by one from the left, starting
        with 1 as the 'default' value to multiply nums[0] with)
        
        and your postfix arr is:
        postfix = [24, 24, 12, 4]
        like the prefix, but starting from the right instead
        
        with this 'memoization', we don't have to do repeat work to find answer
        for nums[i]
        we can just take the prefix value at i - 1  and postfix val at i + 1
        and multiply them together
        
        an additional optimization is that we don't need
        to set up both prefix and postfix arrs
        just compute on the go with the result arr
        """
        
        """
        nums = [1, 2, 3, 4]
        
        first pass of nums, from left to right:
        res = [1, 1, 2, 6] i.e. the prefix
        
        second pass of nums, from right to left:
        
        postfix = 1
        multiply res[3] with 1, we still get [1, 1, 2, 6]
        but now we update postfix to be 1 * nums[3] = 4
        
        postfix = 4
        multiply res[2] with 4, we get [1, 1, 8, 6]
        update postfix to be 4 * nums[2] = 12
        
        postfix = 12
        multiply res[1] with 12, we get [1, 12, 8, 6]
        update postfix to be 12 * nums[1] = 24
        
        postfix = 24
        multiply res[0] with 24, we get [24, 12, 8, 6]
        
        and we're done
        """
        
        res = [1] * (len(nums))
        
        prefix = 1
        # setting up prefix array in res
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        # this is how you decrement from the right in python
        # setting up postfix array
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # this is like multiplying the prefix and postfix tgt
            postfix *= nums[i]
        
        return res
        