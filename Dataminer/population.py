from skiplistclass import SkipList
import math
import csv

class Population(SkipList):
	
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
		dictlist = []
		with open(self.csvfile) as f:
			population = csv.reader(f)

			for row in population:
				# popdict is a dictionary for each row, in which the key is
				# the state ID and the values are another dict called    
				# restofdict
				popdict = {}
				# rest of dict contains all other items of the row except for # state ID
				restofdict = {}

				for i in range(len(row)):
					restofdict[row[i]] = row[i]
					if row[3] in restofdict: 
						del restofdict[row[3]]

				popdict[row[3]] = restofdict
				dictlist.append(popdict)
			# deletes the unnecessary first row of headers in final list
			del dictlist[0]

		print dictlist

if __name__ == '__main__':
	popobj = Population('population.csv')
	popobj.buildPopulation()

