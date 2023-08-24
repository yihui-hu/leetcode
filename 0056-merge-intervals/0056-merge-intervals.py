class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      
      """
      first, sort the intervals via their starting pos
      then, iterate through intervals starting points
      and check for overlaps
      """

      intervals.sort(key = lambda i: i[0])

      # take the first interval and add to output
      output = [intervals[0]] 

      for start, end in intervals[1:]:
        # get most recently added interval
        lastEnd = output[-1][1]

        # means they're overlapping
        if start <= lastEnd:
          # we take the max because of this case: [1, 5], [2, 4] => [1, 5]
          output[-1][1] = max(lastEnd, end)
        else:
          output.append([start, end])
      
      return output