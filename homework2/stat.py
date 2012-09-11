# ECE 2524 Homework 2 Problem 3 Chase Kees

num_records = 0
total_amount_owed = 0

f = open ('/home/chase/Python/database.txt' , 'r')

#Create list to store amount and list for last names
amounts_owed = list()
people_owing = list()

#Loop through and add amounts to the list
for line in f:
	list = line.split()
	#Convert the string to a float before inserting into list
	float_conversion = float(list[2])
	amounts_owed.append(float_conversion)
	people_owing.append(list[1])
	
#Now that we have a list of floats, calculate the amounts needed


#Calculate amount_owed (and figure out how many records there are
for amount in amounts_owed:
	total_amount_owed = total_amount_owed + amount
	num_records = num_records + 1

#Calculate average_owed
average_owed = total_amount_owed / num_records

#Calculate max_owed (start with a numeric value for negative infinity)
#include name so must go back to file and read again
really_small = float ("-inf")
for i, amount in  enumerate(amounts_owed):
	if amount > really_small:
		really_small = amount
		person_max = people_owing[i]
max_owed = really_small

#Calculate min_owed (start with a number value for infinity)
#includes name so must go back to file and read again
really_big = float("inf")
for i, amount in enumerate(amounts_owed):
	if amount < really_big:
		really_big = amount;
		person_min = people_owing[i]
min_owed = really_big

print "ACCOUNT SUMMARY" 
print "Total amount owed =" , total_amount_owed
print "Average amount owed =" , average_owed
print "Maximum amount owed =" , max_owed , "by" , person_max
print "Minimum amount owed =" , min_owed , "by" , person_min


