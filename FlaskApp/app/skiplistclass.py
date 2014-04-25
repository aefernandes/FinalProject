from random import randint, seed
import math
import csv


class SkipNode:
    """A node from a skip list"""    
    def __init__(self, height = 0, elem = None):
        self.elem = elem
        # defines a next element to be pointing to None times the height 
        self.next = [None]*height

class SkipList:

    def __init__(self):
        self.head = SkipNode()
        self.len = 0
        self.maxHeight = 0

    # defines length magic method as an accessor
    def __len__(self):
        return self.len

    def updateList(self, elem):
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update

    def find(self, elem, update = None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None
    

    def populationfind(self, elem, update = None):
        # NEEDS TO GO FROM SKIPLIST TO LIST of DICTS
        dictlist = []
        # creates a list of all found elements
        foundlist = []
        for i in range(len(self.head.next)-1, -1, -1):
            x = self.head
            while x.next[i] != None:
                dictlist.append(x.next[i].elem),
                x = x.next[i]

        for item in dictlist:
            statename = item.keys()
            if item != None and statename[0][0] == elem:
                foundlist.append(item)
                self.remove(item)
        return foundlist


    
    def contains(self, elem, update = None):
        return self.find(elem, update) != None

    def randomHeight(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

        
    def insert(self, elem):

        node = SkipNode(self.randomHeight(), elem)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)            
        if self.find(elem, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1

    def remove(self, elem):

        update = self.updateList(elem)
        x = self.find(elem, update)
        if x != None:
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1            
                
    def printList(self):
        for i in range(len(self.head.next)-1, -1, -1):
            x = self.head
            while x.next[i] != None:
                print x.next[i].elem, 
                x = x.next[i]
            print ''