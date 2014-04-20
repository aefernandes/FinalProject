from skiplistclass import SkipList
import math
import csv

class Population(SkipList):
	"""docstring for Population"""
	def __init__(self, state, name):

# parse the csv, and insert a dictionary of state IDs
# modify find to check for equality of the keys based on State IDs
# override any other important functions