from skiplistclass import SkipList
import csv

class Grants(object):

	def __init__(self, csvfile):
		self.csvfile = csvfile
		self.skiplist = SkipList()

	# parse the csv, and create a list of dictionaries
	# each element has a key of awardee name, and the values
	# are the rest of the columns.

	def buildGrants(self):
		# opens the csv file and this is the main method that builds 
		# the skiplist of dicts for population
		dictlist = []
		with open(self.csvfile) as f:
			grants = csv.reader(f)

			headers = next(grants)

			for row in grants:
				# grantdict is a dictionary for each row, in which the key is
				# the awardee name and the values are another dict called    
				# restofdict
				grantdict = {}
				# rest of dict contains all other items of the row except for # state ID
				restofdict = {}

				# builds the restofdict using header names as keys
				# deletes unnecessary awardee, value pair
				for i in range(len(row)):
					restofdict[headers[i]] = row[i]
					if 'Awardee' in restofdict: 
						del restofdict['Awardee']

				grantdict[row[0]] = restofdict
				# appends to the list of dictionaries
				dictlist.append(grantdict)
			# deletes the unnecessary first row of headers in final list
			del dictlist[0]

		return dictlist

# Testing that the module works standalone and inserts appropriately
if __name__ == '__main__':
	grantobj = Grants('researchgrants.csv')
	grantlist = grantobj.buildGrants()
	for item in grantlist:
		grantobj.skiplist.insert(item)

	grantobj.skiplist.printList()