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
print("Starting")
Sev_species(data, ['Drosophila melanogaster', 'Drosophila simulans'])
print("Finished with first Ex")
Len_range(data, 90,110)
print("Finished with second Ex")
