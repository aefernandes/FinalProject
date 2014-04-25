from builder import Builder
from skiplistclass import SkipList  
import csv

# filters the skiplist and returns a filtered CSV file
# takes in a skiplist and a dict of parameters to filter by
def makeFilteredPop(sklist, postreqdict):
    if 'initial' in postreqdict:
        initialvalue = postreqdict['initial']

    filtereditem = sklist.populationfind(initialvalue)
    # debuggging for now
    for thing in filtereditem:
        print thing



