class Solution:
    def search(self, nums: List[int], target: int) -> int:
      """
      first, find pivot index using binary search
      then, once found, perform binary search on both 'splits'
      time complexity will be O(3 * log n) = O(log n)
      """

      left, right = 0, len(nums) - 1 

      while left <= right:
        middle = (left + right) // 2
        if nums[middle] > nums[len(nums) - 1]:
          left = middle + 1
        else:
          right = middle - 1

      # we found pivot
      pivot = left
      print(pivot)

      firstL, firstR = 0, pivot - 1
      secondL, secondR = pivot, len(nums) - 1

      while firstL <= firstR:
        middle = (firstL + firstR) // 2
        if nums[middle] > target:
          firstR = middle - 1
        elif nums[middle] < target:
          firstL = middle + 1
        else:
          return middle
      
      while secondL <= secondR:
        middle = (secondL + secondR) // 2
        if nums[middle] > target:
          secondR = middle - 1
        elif nums[middle] < target:
          secondL = middle + 1
        else:
          return middle

      return -1
      