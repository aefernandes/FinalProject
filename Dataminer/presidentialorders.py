from skiplistclass import SkipList
import csv

class PresidentialOrders(object):

	def __init__(self, csvfile):
		self.csvfile = csvfile
		self.skiplist = SkipList()

	# parse the csv, and create a list of dictionaries
	# each element has a key of a state ID, and the values
	# are the rest of the columns.

	def buildPresidentialOrders(self):
		# opens the csv file and this is the main method that builds 
		# the skiplist of dicts for population
		dictlist = []
		with open(self.csvfile) as f:
			orders = csv.reader(f)

			headers = next(orders)

			for row in orders:
				# popdict is a dictionary for each row, in which the key is
				# the name of the order and the values are another dict called    
				# restofdict
				ordersdict = {}
				# rest of dict contains all other items of the row except for # state ID
				restofdict = {}

				# builds the restofdict using header names as keys
				# deletes unnecessary name element
				for i in range(len(row)):
					restofdict[headers[i]] = row[i]
					if 'title' in restofdict: 
						del restofdict['title']

				ordersdict[row[1]] = restofdict
				# appends to the list of dictionaries
				dictlist.append(ordersdict)
			# deletes the unnecessary first row of headers in final list
			del dictlist[0]

		return dictlist

# Testing that the module works standalone and inserts appropriately
if __name__ == '__main__':
	ordersobj = PresidentialOrders('presidentialdocuments.csv')
	orderslist = ordersobj.buildPresidentialOrders()
	for item in orderslist:
		ordersobj.skiplist.insert(item)

	ordersobj.skiplist.printList()