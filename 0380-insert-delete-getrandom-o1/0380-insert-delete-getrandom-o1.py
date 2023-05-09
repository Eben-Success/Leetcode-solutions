class RandomizedSet:
    
    """
    {1: 0, 4; 1, 5: 2 }
    [1, (index 1:10), 5, 7, 9, 10] => remove(4)
    """

    def __init__(self):
        self.arr = []
        self.hashmap = {}
        

    def insert(self, val: int) -> bool:
        
        if val in self.hashmap:
            return False
        
        self.hashmap[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        
        if val not in self.hashmap:
            return False
        
        idx = self.hashmap[val]
        last = self.arr[-1]
    
        self.arr[idx] = last
        self.hashmap[last] = idx
        self.arr.pop()
        del self.hashmap[val]
        return True
        
        
        

    def getRandom(self) -> int:
        
        return random.choice(self.arr)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()