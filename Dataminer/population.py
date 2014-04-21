from skiplistclass import SkipList
import math
import csv

class Population(SkipList):
	"""docstring for Population"""
	def __init__(self, csvfile):
		self.csvfile = csvfile

# parse the csv, and create a list of dictionaries
# each element has a key of a state ID, and the values
# are the rest of the columns.

# for each in dictlist, insert each as a node. Return the skiplist 
# define the state ID's for the user lookup later

# modularizing a buildPopulation function to simplify the code in main.py
	def buildPopulation(self):
		# opens the csv file and this is the main method that builds 
		# the skiplist of dicts for population
		with open(self.csvfile) as f:
			population = csv.reader(f)
			for row in population:
				# insert row[3] as keys of a dict
				# insert rest of names as keys, and rest of everything
				# as values

if __name__ == '__main__':
	popobj = Population('population.csv')
	popobj.buildPopulation()

