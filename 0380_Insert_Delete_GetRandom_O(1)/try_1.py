class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        ret = val not in self.set
        self.set.add(val)
        return ret

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        ret = val in self.set
        if ret:
            self.set.remove(val)
        return ret
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.sample(self.set, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()