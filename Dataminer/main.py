from population import Population 
import csv
import math

################# DATA MINER ####################
#                                               #
#      Makes a dataminer for government data    #
#      that outputs useful CSV files for easy   #
#      data manipulation                        #
#################################################   

# First, defines the 3 builder functions

# makes the population skiplist
def makepopulationlist():
    popobj = Population('population.csv')
    populationlist = popobj.buildPopulation()

    for item in populationlist:
        popobj.skiplist.insert(item)

    return popobj.skiplist

def makeDATASET2list():

def makeDATASET3list():


def main():

    # CHECK for user input
    if CHOICE == POPULATION:
        popskiplist = makepopulationlist()
        print "Built the population list successfully!\n"

    elif CHOICE == DATASET2:
        DATASET2skiplist = makeDATASET2list()
        print "Built the DATASET2 list successfully!\n"
    else:
        DATASET3skiplist = makeDATASET3list()
        print "Built the DATASET3 list successfully!\n"

    # Redirect
    # to another page where the user can actually search

    # now in the search page, there will be search boxes
    # corresponding to the data at hand. For example,
    # for population, we can search for state, or search by
    # range of populations

main()