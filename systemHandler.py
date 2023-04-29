import sys
import os

filePath = ""

'''findFile gets the computer name and finds the data file located with it'''
def getFile():
	if filePath != "":
		return filePath
	"""
	get pc name
	check ./data/pcnameHASH.csv
	catch(filenotfoundexception):
		createFile()
	filePath = file.path

	"""

'''Creates a file if a data file does not exist'''
def createFile():
	'''
	os/sys file creation w hash
	'''
