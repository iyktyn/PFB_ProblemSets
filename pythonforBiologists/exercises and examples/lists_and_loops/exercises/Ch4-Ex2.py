#! /usr/bin/env python

import sys

DNA = open(sys.argv[1]).read()
ExonFile = open(sys.argv[2])

DNA_Exon = open("DNA_Exon.txt", 'a')

for Exon in ExonFile.readlines():
	ExonList = Exon.split(',')
	start =  int(ExonList[0])
	end = int(ExonList[1])
	DNA_Exon.write(DNA[start:end])


ExonFile.close()
DNA_Exon.close()
