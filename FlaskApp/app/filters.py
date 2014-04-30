from builder import Builder
from skiplistclass import SkipList  
import csv
import helpers

def remove_duplicate_dictlist(dictlist):
    output = []
    for x in dictlist:
        if x not in output:
            output.append(x)
    return output

# filters the skiplist and returns a filtered CSV file
# takes in a skiplist and a dict of parameters to filter by
def InitialFilterPop(sklist, postreqdict):
    if 'initial' in postreqdict:
        initialvalue = postreqdict['initial']

    filteredlist = sklist.populationfind(initialvalue)
    precsvlist = []

    for elem in filteredlist:

        # creates a single huge dictionary for 
        # the csv dict writer to work well
        singledictionary = {}

        namelist = elem.keys()
        singledictionary['NAME'] = namelist[0]

        importantvals = elem.values()
        singledictionary.update(importantvals[0])

        # creates a list of all these single dictionaries
        # to make it easy for the csv to work
        precsvlist.append(singledictionary)
    
    # creates a unique list free of duplicates
    uniquelist = remove_duplicate_dictlist(precsvlist)

    # makes a csv with the uniquelist
    helpers.PopulationCSV(uniquelist, 'initial')
 
 
