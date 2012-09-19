from sys import argv
import argparse
import sys
import fileinput

parser = argparse.ArgumentParser(description = "Process some numbers.")
parser.add_argument('infile', nargs='*')
args = parser.parse_args()

multiply = 1
for line in fileinput.input(args.infile):
	try:
		newVal = line
		if(newVal == "\n"):
			#Here would have if statement for --ignore-blank
			#if it is there
			continue
			#else would do this
			#print multiply
			#multiply = 1
			#continue
		
		numVal = int(newVal)
		multiply = multiply*numVal
	except EOFError:
		break;
	except ValueError:
		#Here would have an if statement for --ignore-non numeric
		#if it is there
		continue
		#else do the following
		#sys.stderr.write("Could not convert string to float: %s\n" % newVal)
		#sys.exit(1)
		
print multiply
	

	


	
	



