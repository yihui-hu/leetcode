class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        """
        brute force:
        iterate over all intervals
        once we reach an interval with a start <= newstart and end >= newstart,
        we begin the merge (needs <= and >= because start/end may be same)
        if the new interval overlaps multiple intervals,
        maybe create new array and add the necessary intervals to it
        not good for space complexity but ok
        """

        res = []

        for i in range(len(intervals)):
          # two conditions are for if both conditions don't overlap
          if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
          elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
          else:
            # merging intervals with overlap
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)

        return res
      