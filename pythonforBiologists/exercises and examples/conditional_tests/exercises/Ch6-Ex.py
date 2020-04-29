#! /user/local/bin python

import csv

with open('data.csv', newline='') as f:
	reader = csv.reader (f)
	data = list(reader)


def Sev_species(csv, species):
	for line in csv:
		if line[0] in species:
			print(line[2])

def Len_range(csv, low = 0, high = 500):
	for line in csv:
		if len(line[1]) > low and len(line[1]) < high:
			print(line[2])

def AT_content(seq):
	seq = seq.upper()
	count = 0
	for base in seq:
		if base == 'A' or base == 'T':
			count =+ 1
	AT_cont = count / len(seq)
	return AT_cont

def AT_content_and_expression(csv,exp):
	for line in csv:
		if AT_content(line[1]) < 0.5 and int(line[3]) > exp:
			print(line[2])

def Complex_cond(csv):
	for line in csv:
		if (line[2][0] == 'k' or line[2][0] == 'h') and line[0] != 'Drosophila melanogaster':
			print(line[2])

print("Starting")
Sev_species(data, ['Drosophila melanogaster', 'Drosophila simulans'])
print("Finished with first Ex")
Len_range(data, 90,110)
print("Finished with second Ex")
AT_content_and_expression(data,200)
print("Finished with third Ex")
Complex_cond(data)
print("Finished with fourth Ex")
