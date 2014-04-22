from skiplistclass import SkipList
import math
import csv

class Population(object):

	def __init__(self, csvfile):
		self.csvfile = csvfile
		self.skiplist = SkipList()

	# parse the csv, and create a list of dictionaries
	# each element has a key of a state ID, and the values
	# are the rest of the columns.

	def buildPopulation(self):
		# opens the csv file and this is the main method that builds 
		# the skiplist of dicts for population
		dictlist = []
		with open(self.csvfile) as f:
			population = csv.reader(f)

			headers = next(population)

			for row in population:
				# popdict is a dictionary for each row, in which the key is
				# the state ID and the values are another dict called    
				# restofdict
				popdict = {}
				# rest of dict contains all other items of the row except for # state ID
				restofdict = {}

				# builds the restofdict using header names as keys
				# deletes unnecessary state ID key, value pair
				for i in range(len(row)):
					restofdict[headers[i]] = row[i]
					if 'STATE' in restofdict: 
						del restofdict['STATE']

				popdict[row[3]] = restofdict
				# appends to the list of dictionaries
				dictlist.append(popdict)
			# deletes the unnecessary first row of headers in final list
			del dictlist[0]

		return dictlist

# Testing that the module works standalone and inserts appropriately
if __name__ == '__main__':
	popobj = Population('population.csv')
	populationlist = popobj.buildPopulation()
	for item in populationlist:
		popobj.skiplist.insert(item)

	popobj.skiplist.printList()