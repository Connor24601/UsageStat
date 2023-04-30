import os
import sys
import subprocess

import systemHandler
import dataHandler


def handleBash(bashCommand):
	'''takes a bash Command and runs it and returns the result'''
	try:
		output, error = (None, None)
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
	except Exception as e:
		print("There was a problem running command : " + bashCommand)
		print(e)
		return None
	finally:
		if (error != None):
			print("There was an error running command: " + bashCommand)
			print ("Error: " + error)
			return None
		if (output != None):
			return output.decode()
		return None