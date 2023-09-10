class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for num in nums:
          if num in map:
            map[num] += 1
          else:
            map[num] = 1
        
        # sort by values

        iterable_map = sorted(map.items(), key=lambda x:x[1], reverse=True)

        print(iterable_map)

        res = []
        # iterable_map = list(map)
        for i in range(k):
          res.append(iterable_map[i][0])
        
        return res
