from builder import Builder
import csv
import math
import sys

################# DATA MINER ####################
#                                               #
#      Makes a dataminer for government data    #
#      that outputs useful CSV files for easy   #
#      data manipulation                        #
#################################################   

# First, defines the 3 builder functions

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


def main():

    choice = raw_input("What kind of skip list do you want to build? \
                        Population, PresidentialOrders, or ResearchGrants? \
                        [1/2/3]\n")
    # CHECK for user input
    if choice == "1":
        popskiplist = makePopulationlist()
        print "Built the population list successfully!\n"

        question = raw_input("Want to print it out? [Y/N]\n")
        if question == "Y" or "y":
            popskiplist.printList()

    elif choice == "2":
        presidentialskiplist = makePresidentialOrderlist()
        print "Built the presidential document list successfully!\n"

        question = raw_input("Want to print it out? [Y/N]\n")
        if question == "Y" or "y":
            presidentialskiplist.printList()

    elif choice == "3":
        grantskiplist = makeGrantlist()
        print "Built the research grant list successfully!\n"

        question = raw_input("Want to print it out? [Y/N]\n")
        if question == "Y" or "y":
            grantskiplist.printList()

    else:
        print "Oops, not the correct choice"

    # Redirect
    # to another page where the user can actually search

    # now in the search page, there will be search boxes
    # corresponding to the data at hand. For example,
    # for population, we can search for state, or search by
    # range of populations

main()