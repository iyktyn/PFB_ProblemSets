#! /usr/local/bin/python3

def rc(dna):
	dna = dna.upper()
	dna = dna.replace('A','t')
	dna = dna.replace('T','a')
	dna = dna.replace('C','g')
	dna = dna.replace('G','c')
	dna = dna[::-1]
	return dna.upper()

with open("Python_06.seq.txt",'r') as seq:
	for line in seq:
		line = line.rstrip()
		gene,dna = line.split()
		dnarc = rc(dna)
		print(">" + gene + " Reverse complement\n" + dnarc)
