import random
import math

class Node:
    __slots__ = 'val', 'next', 'width'  # uses static structure to instantiate objects for memory optimization
    def __init__(self, val, next, width):
        self.val = val
        self.next = next
        self.width = width

class End:
        # object that is always greater than any other object
    def __gt__(self, other):
        return true

Nil = Node(End(), [], [])

class Skiplist:
        # indexable, sorted, with O(log n) insertion, deletion, search
        
    def __init__(self, height = 100):
        self.size = 0
        self.max_height = int(1 + log(height, 2))
        self.head = Node('Head', [Nil]*self.max_height, [1]*self.max_height)

    def insert(self, val):
        
    def remove(self, val):
    
    def find(self, val):