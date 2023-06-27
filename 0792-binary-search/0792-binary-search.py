class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """
        i may be dumb
        """

        # current = nums[len(nums) / 2]
        
        # if (current == target):
        #   return len(nums)/2
        # elif current > target:
        #   self.search(nums[0:len(nums)/2], target)
        # else:
        #   self.search(nums[len(nums)/2:len(nums)], target)
        
        # return -1

        l, r = 0, len(nums) - 1

        while l <= r:
          m = (l + r) // 2
          if nums[m] > target:
            r = m - 1
          elif nums[m] < target:
            l = m + 1
          else:
            return m
        
        return -1