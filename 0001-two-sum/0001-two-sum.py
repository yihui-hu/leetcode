class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        1. use hash map
        2. store as value : index
        """

        """
        edge cases:
        1. negative numbers
        2. duplicate numbers (should be ok as long as we iterate)
        """

        prevMap = {} # mapping value : index

        # loop through array of nums
        for index, value in enumerate(nums):
            # get difference between target and current num
            difference = target - value
            # if difference exists in hash map, great, return both indices
            if difference in prevMap:
                return [prevMap[difference], index]
            # else, add current value and its index to hash map
            prevMap[value] = index

        return []
        