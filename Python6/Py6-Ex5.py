#! /usr/local/bin/python3

import sys

fastafile = sys.argv[1]

def fastadict(fasta):
	fdict = {}
	lastkey = "none"
	lastsequence = "empty"
	for line in fasta:
		line = line.rstrip()
		if line[0] == ">":
			fdict[lastkey] = lastsequence
			lastkey = line[1:]
			lastsequence = ""
		else:
			lastsequence = lastsequence + line			
#		print("Added" + lastkey + " " + lastsequence)
#		print(fdict)
	fdict[lastkey] = lastsequence
#	print(fdict)
	del fdict["none"]
	return fdict

with open(fastafile, 'r') as fasta:
	output = fastadict(fasta)

print(output) 
