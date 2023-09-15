class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        use two pointers, one at start and end
        move them according to if theyre bigger / smaller than targer
        """

        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
          if numbers[left] + numbers[right] > target:
            right -= 1
          else:
            left += 1

        return [left + 1, right + 1]