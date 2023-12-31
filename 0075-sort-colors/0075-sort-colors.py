class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        we can use bucketsort because we know 
        the range of values
        """

        """
        interesting quicksort implementation:
        https://www.youtube.com/watch?v=4xbWSRZHqac
        """

        bucket = [0, 0, 0]

        for value in nums:
          bucket[value] += 1

        numsIndex = 0

        for i in range(len(bucket)):
          while bucket[i] > 0:
            nums[numsIndex] = i
            bucket[i] -= 1
            numsIndex += 1
        
        return nums
