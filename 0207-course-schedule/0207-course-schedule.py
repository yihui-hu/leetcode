class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        """
        if there is cycle, we know that we cannot fulfill reqs,
        use a set to keep track of visited nodes; if we visited a node
        again, there's a cycle

        we want to perform DFS on course 0 and reach a course 
        where there are no prerequisites, which we can then mark
        as complete, and then we escape out from there
        """

        preMap = { i:[] for i in range(numCourses) } # create adj list of courses and pre requisites
        # for every course, map it to an empty list
        
        for course, pre in prerequisites:
          preMap[course].append(pre) # for each course, append the prereq to the empty list we initialised above

        visited = set() # store courses along the DFS path

        def dfs(course):
          if course in visited: # means we detected a loop
            return False
          if preMap[course] == []: # empty list meanas no prereq
            return True
          
          visited.add(course)
          for prereq in preMap[course]:
            if not dfs(prereq): # if this ever returns false, we can immediately return true, no need to wait
              return False

          visited.remove(course) # remove course from the set because we've already finished visiting it
          preMap[course] = [] # set to empty list because if we run DFS on it again, then we don't have to redo the work
          return True  

        """
        note: we have to perform DFS on *every* course in numCourses (not just the starting course) because the graphs may be disjoint, e.g.:
        
        1 --> 2
        3 --> 4

        where --> indicates a dependency
        """

        for course in range(numCourses):
          if not dfs(course): # perform DFS on each course in numCourses, returning false immediately if one of the recursions returns false
            return False
        
        return True