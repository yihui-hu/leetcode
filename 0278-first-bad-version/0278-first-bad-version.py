# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        this is a variation of binary search
        """

        left, right = 0, n
        earliest_bad_version = 0

        while left <= right:
          middle = (left + right) // 2
          # search in the right
          if isBadVersion(middle):
            right = middle - 1
            earliest_bad_version = middle
          else:
            left = middle + 1
          
        return earliest_bad_version
