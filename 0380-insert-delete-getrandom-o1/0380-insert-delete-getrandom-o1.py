class RandomizedSet:

    def __init__(self):
        # map keeps track of membership of element
        # values keeps track of actual elements
        self.values = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
          return False
        
        self.values.append(val)
        # store index in map
        self.map[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
          return False
        
        # to enable O(1) removal, we do some swapping
        val_to_remove_index = self.map[val]
        val_at_last_index = self.values[-1]
        self.values[-1] = val
        self.values[val_to_remove_index] = val_at_last_index
        self.map[val_at_last_index] = val_to_remove_index
        self.values.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()