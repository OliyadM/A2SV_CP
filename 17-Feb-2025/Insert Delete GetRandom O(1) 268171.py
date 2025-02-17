# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        self.lst = []

    def insert(self, val):
        if val in self.map:
            return False
        self.map[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val):
        if val not in self.map:
            return False
        
        idx = self.map[val]
        last = self.lst[-1]
        
        self.lst[idx] = last
        self.map[last] = idx
        
        self.lst.pop()
        del self.map[val]
        
        return True

    def getRandom(self):
        return random.choice(self.lst)

