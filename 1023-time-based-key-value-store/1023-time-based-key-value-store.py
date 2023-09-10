class TimeMap(object):

    def __init__(self):
        self.map = {} # key : list of [value, timestamp]

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        # if key in self.map:
        #   self.map[key][timestamp] = value
        # else:
        #   self.map[key] = {}
        #   self.map[key][timestamp] = value

        if key not in self.map:
          self.map[key] = []
        self.map[key].append([value, timestamp])


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        res = ""

        # get value from map if key exists, else return empty list
        values = self.map.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
          m = (l + r) // 2
          if values[m][1] <= timestamp:
            res = values[m][0]
            l = m + 1
          else:
            r = m - 1
        
        return res

        # if key in self.map:
        #   while timestamp >= 1:
        #     if timestamp in self.map[key]:
        #       return self.map[key][timestamp]
        #     timestamp -= 1
        
        # return ""

        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)