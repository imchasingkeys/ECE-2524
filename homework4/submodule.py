#Submodule file
import fileinput
import sys
import re
import operator
from operator import itemgetter, attrgetter
from pprint import pprint


def getRecordList(filename):
	recordList = list()
	for line in fileinput.input(filename):
		recordList.append(line)
	return recordList
 
def createDictionary(filename):
	listRecords = getRecordList(filename)
	listOfDictionaries = list()
	for record in listRecords:
		dictionary = {}
		split = record.split(",")
		for pair in split:
			split2 = pair.split(":")
			dictionary[split2[0]] = split2[1]
		#Now that this dictionary is made add to list
		listOfDictionaries.append(dictionary)
	return listOfDictionaries

def listStuff(command, filename):
	split = command.split()
	if "sort" in command:
		if not len(split) == 4:
			print "Please list a valid attribute after list all sort"
			return
		attribute = split[3]
		if(attribute == "PartID"):
			listNum = 0
		elif(attribute == "Description"):
			listNum = 1
		elif(attribute == "Quantity"):
			listNum = 3
		elif(attribute == "Footprint"):
			listNum = 2
		else:
			print "Error: Attribute listed is not valid"
			return
		attribute = "'" + attribute + "'"
	
		listRecordsDictionaries = createDictionary(filename)

		listRecordsDictionaries.sort(key=operator.itemgetter(attribute))	
		sys.stdout.write("<DATA>\n")
		for record in listRecordsDictionaries:
			sys.stdout.write( "'PartID':" + record["'PartID'"] + ",'Description':" + record["'Description'"] + \
			      ",'Footprint':" + record["'Footprint'"] + ",'Quantity':" + record["'Quantity'"]	)
		sys.stdout.write("\n")

	elif len(split) > 2:
		attributeAndValue = split[2]
		listRecords = getRecordList(filename)
		attributeAndValueList = attributeAndValue.split(":")
		attribute = attributeAndValueList[0]
		valueChosen = attributeAndValueList[1]
		listNum = 0
		if(attribute == "PartID"):
			listNum = 0
		elif(attribute == "Description"):
			listNum = 1
		elif(attribute == "Quantity"):
			listNum = 3
		elif(attribute == "Footprint"):
			listNum = 2
		else:
			print "Error: Attribute listed is not valid"
			return
		#Now list all that have the matching value for this attribute
		found = False
		sys.stdout.write("<DATA>\n")
		for record in listRecords:
			pairs = record.split(",")
			pair = pairs[listNum]
			values = pair.split(":")
			value = values[1]
			value = value.replace("'", "")
			if value == valueChosen:
				sys.stdout.write(record)
				found = True
		if found == False:
			print "Error: Value was not found"
		sys.stdout.write("\n")

	else:
		sys.stdout.write("<DATA>\n")
		for line in fileinput.input(filename):
			sys.stdout.write(line)
		sys.stdout.write("\n")

def add(command, filename):
	addArgs = command.split()
	addArgs.remove("add")
	with open(filename, "a") as myfile:
		for arg in addArgs:
			myfile.write(arg)
	print "Record was added"

def remove(command, filename):
	listRecords = list()
	listRecords = getRecordList(filename)
	PartId = command.split()
	PartId.remove("remove")
	found = False
	count = 0;
	for record in listRecords:
		if record == "\n":
			del listRecords[count]
			continue
		item = record.split(",")
		fileId = item[0].split(":")
		IdinFile = fileId[1].replace("'", "")
		if(IdinFile == PartId[0]):
			del listRecords[count]
			found = True
			ID = IdinFile
		count = count + 1
	
	#Now that matching records are removed, re-print to file
	with open(filename, "w") as myfile:
		myfile.write("".join(str(x) for x in listRecords))
	if(found != True):
		print "Error: Not a valid Part ID"
	elif(found == True):
		print "PartID:%s was removed" %ID
		

def set(command, filename):
	split = command.split()
	listRecords = getRecordList(filename)
	Pair1 = split[1]
	Pair2 = split[2]
	Pair1List = Pair1.split(":")
	Pair2List = Pair2.split(":")
	attribute1 = Pair1List[0]
	attribute2 = Pair2List[0]
	value1 = Pair1List[1]
	value2 = Pair2List[1]

	attribute2 = "'" + attribute2 + "'"
	value2 = "'" + value2 + "'"
	PairtoCheck = attribute2 + ":" + value2
	


	attribute1 = "'" + attribute1 + "'"
	value1 = "'" + value1 + "'"
	PairtoAdd = attribute1 + ":" + value1
	anyValue = "'.*?'"
	PairtoRemove = attribute1 + ":" + anyValue
	
	count = 0
	for record in listRecords:
		if PairtoCheck in record:
			listRecords[count] = re.sub(PairtoRemove, PairtoAdd, record)
		count = count + 1
	#Now print the records
	with open(filename, "w") as myfile:
		myfile.write("".join(str(x) for x in listRecords))
	print "Record was updated"
			
	
	








