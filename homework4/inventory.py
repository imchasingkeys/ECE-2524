#HW4
#Chase Kees
#Intro UNIX

import argparse
import fileinput
import sys
import submodule


parser = argparse.ArgumentParser(description='Store and manipulate records')
parser.add_argument('-f', '--data-file', help='Path to the data file of actions to read at startup', required =True)
args = parser.parse_args()

for line in sys.stdin:
	newVal = line;
	if "list all" in newVal:
		submodule.listStuff(newVal, args.data_file)	
	elif "add" in newVal:
		submodule.add(newVal, args.data_file)
	elif "remove" in newVal:
		submodule.remove(newVal, args.data_file)
	elif "set" in newVal:
		submodule.set(newVal, args.data_file)
	else:
		print "Not a valid command"


