from builder import Builder
from skiplistclass import SkipList  
import csv

# filters the skiplist and returns a filtered CSV file
# takes in a skiplist and a dict of parameters to filter by
def makeFilteredPop(sklist, postreqdict):

    precsvlist = []
    i = sklist.len
    while i >= 0:
        eleminitial = sklist.populationfind('population', 'initial', postreqdict['initial'])
        if eleminitial not in precsvlist:
            precsvlist.append(eleminitial)
            print precsvlist

        elemgreater = sklist.populationfind('population', 'popgreater', postreqdict['popgreater'])
        if elemgreater not in precsvlist:
            precsvlist.append(elemgreater)

        elemlesser = sklist.populationfind('population', 'poplesser', postreqdict['poplesser'])
        if elemlesser not in precsvlist:
            precsvlist.append(elemlesser)

        sklist.remove(eleminitial)
        sklist.remove(elemgreater)
        sklist.remove(elemlesser)
        i -= 3
 
    with open('filtereddata.csv', 'w') as f:
    # writes the csv from the filtered skiplist above
        writer = csv.writer(f, delimiter = ',')
        writer.writerow(precsvlist)

 

