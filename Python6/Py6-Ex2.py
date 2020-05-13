#! /usr/local/bin/python3
#Adding for testing

with open("Python_06.txt",'r') as text, open("Python_06_uc.txt",'w') as output:
	for line in text:
		line = line.rstrip().upper()
		output.write (line + "\n")
