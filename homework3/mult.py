from sys import argv
import argparse
import sys

parser = argparse.ArgumentParser(description = "Process some numbers.")
args = parser.parse_args()

multiply = 1
while 1:
	try:
		newVal = raw_input()
		if(newVal == ""):
			print multiply
			multiply = 1
			continue
		
		numVal = int(newVal)
		multiply = multiply*numVal
	except EOFError:
		break;
	except ValueError:
		sys.stderr.write("Could not convert string to float: %s\n" % newVal)
		sys.exit(1)
		
print multiply
	

	


	
	



