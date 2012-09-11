# ECE 2524 Homework 2 Problem 1 Chase Kees

f = open('/etc/passwd', 'r')

for line in f:
	list = line.split(':')
	print list[0], "\t" , list[6]
	
