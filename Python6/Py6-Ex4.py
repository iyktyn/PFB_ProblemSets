#! /usr/local/bin/python3

with open("Python_06.fastq",'r') as fastq:
	lines = 0
	chars = 0

	for line in fastq:
		lines += 1
		chars += len(line)
	print("The total number of lines is " + str(lines) + " and the total number of characters is " + str(chars) +" and the average line length is " + str(chars/lines) + ".")
