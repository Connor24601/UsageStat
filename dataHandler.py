import csv
import time
import systemHandler

'''This function writes data into the CSV'''
def writeData(data):
	# getter
	filePath = systemHandler.getFile()
	with open(filePath,"w") as doc:
		cdoc = csv.reader(doc)


def format(isStartup):
	# test

time.ctime()

def checkData():
	filePath = systemHandler.getFile()
	with open(filePath, "r") as doc:
		# TODO: add actual parsing here
		if (last line contains uptime):
			main.promptUser()
		

