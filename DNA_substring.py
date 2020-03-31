#Prints a substring of DNA

import sys

dna = sys.argv[1]
first =int(sys.argv[2])
second =int(sys.argv[3])

#Converts the inputed starting bp to be -1 of orginal
first =  first - 1
#Finds the DNA substring requested
dna_sub = dna[first:second]

#Prints the DNA substring
print(dna_sub)

#Counts the Gs in the substring
g_count = dna_sub.upper().count('G')

print('Your substring has {} number of Gs'.format(g_count))
