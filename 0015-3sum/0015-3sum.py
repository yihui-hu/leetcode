class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        """
        sort the input array first: this is important because we want to
        memoize the entries that we fill in the three 'slots' that add up to our sum
        
        e.g. [-3, -3, 1, 2, 3, 4], target = 0
        assume we've already found one triplet:
        a = -3
        b = 1
        c = 2
        on the next iteration,
        a = -3, we already had -3 in our previous iteration
        so we skip this
        
        then, reduce the problem down to two sum II when finding b and c
        
        time complexity: sorting will take O(n log n), and using one loop to inform a, and another loop to inform b and c, so that's O(n^2) and in total it'll be O(n^2)
        space: O(1) or O(n) depending on sorting libraries (merge sort is O(n))
        """
        
        res = []
        nums.sort()
        
        # one potential optimization: check if first elem is > 0, if so, return
        if (len(nums) > 0):
            if (nums[0] > 0):
                return res
        
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]: # means it's a repeat value
                continue
            
            l, r = index + 1, len(nums) - 1
            while l < r:
                currSum = value + nums[l] + nums[r]
                if (currSum > 0):
                    r -= 1
                elif (currSum < 0):
                    l += 1
                else:
                    res.append([value, nums[l], nums[r]]) # update results array
                    
                    # update pointers, ONLY for this two sum II part of the problem
                    # essentially we fix a, but we want to make sure
                    # we cover all bs and cs that make it add up to 0
                    # also we only shift left pointer because
                    # the if loops above cover the other pointer
                    
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:  
                        # account for same vals
                        # and l must not cross r
                        l += 1
        
        return res