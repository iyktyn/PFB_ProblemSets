#! /usr/local/bin/python3

with open("Python_06.txt",'r') as text:
	for line in text:
		line = line.rstrip().upper()
		print(line)
