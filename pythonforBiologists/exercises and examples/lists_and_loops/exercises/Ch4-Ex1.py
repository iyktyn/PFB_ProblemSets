#! /usr/bin/env python

import sys

input_file = open(sys.argv[1])

output_file = open("output.txt", 'a')

for line in input_file:
	new_line = line[14:]
	output_file.write(new_line)
	print("The new line lenght is: " + str(len(new_line)))

input_file.close()
output_file.close()	
