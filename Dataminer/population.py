from skiplistclass import SkipList
import math
import csv

class Population(SkipList):
	"""docstring for Population"""
	def __init__(self, state, name):

# parse the csv, and create a list of dictionaries
# each element has a key of a state ID, and the values
# are the rest of the columns.

# for each in dictlist, insert each as a node. Return the skiplist 
# define the state ID's for the user lookup later

# modularizing a buildPopulation function to simplify the code in main.py
	def buildPopulation(file):
		# opens the csv file and this is the main method that builds 
		# the skiplist of dicts for population
		with open(file) as f:
