from builder import Builder
import csv

################# DATA MINER ####################
#                                               #
#      Makes a dataminer for government data    #
#      that outputs useful CSV files for easy   #
#      data manipulation                        #
#################################################   

# Helper Functions

# makes the population skiplist
def makePopulationlist():
    
    popobj = Builder('population.csv', 4, 'NAME')
    populationlist = popobj.build()
    for item in populationlist:
        popobj.skiplist.insert(item)

    return popobj.skiplist

def makePresidentialOrderlist():
   
    ordersobj = Builder('presidentialdocuments.csv', 1, 'title')
    orderslist = ordersobj.build()
    for item in orderslist:
        ordersobj.skiplist.insert(item)

    return ordersobj.skiplist



def makeGrantlist():
    grantobj = Builder('researchgrants.csv', 0, 'Awardee')
    grantlist = grantobj.build()

    for item in grantlist:
        grantobj.skiplist.insert(item)

    return grantobj.skiplist

# removes all duplicates from a list of dictionaries
def remove_duplicate(dictlist):
    output = []
    for x in dictlist:
        if x not in output:
            output.append(x)
    return output


def CSVmaker(uniquelist):
    
    # gets the rownames from any element of the list of dicts
    rownames = uniquelist[0].keys()
    with open('filtereddata.csv', 'wb') as f:
        writervar = csv.writer(f)
        writervar.writerow(rownames)

        for row in uniquelist:
            valtowrite = row.values()
            writervar.writerow(valtowrite)




