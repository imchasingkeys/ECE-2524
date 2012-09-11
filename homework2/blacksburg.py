# ECE 2524 Homework 2 Problem 2 Chase Kees

# I just pointed the open function to where the file was on my pc
# since it didn't say to set it to a certain path in the HW description
f = open('/home/chase/Python/database.txt' , 'r')


print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS" 

for line in f:
	
	list = line.split()
	if list[3] == "Blacksburg":
		#print list[4],", " , list[1] , ", " , list[0] , ", " , list[2]
		printList = [list[4], list[1], list[0], list[2]]
		commaString = ", "
		print commaString.join(printList)
	


