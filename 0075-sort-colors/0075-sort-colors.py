class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        we can use bucketsort because we know 
        the range of values
        """

        bucket = [0, 0, 0]

        for value in nums:
          bucket[value] += 1

        numsIndex = 0

        print(bucket)
        for i in range(len(bucket)):
          while bucket[i] > 0:
            nums[numsIndex] = i
            bucket[i] -= 1
            numsIndex += 1
        
        return nums
