#! /usr/local/bin/env python3
import sys

dna = sys.argv[1]

dna_upper = dna.upper()

a_count = dna_upper.count('A')
t_count = dna_upper.count('T')
c_count = dna_upper.count('C')
g_count = dna_upper.count('G')

print('There are {} As and {} Ts and {} Cs and {} Gs'.format(a_count, t_count, c_count, g_count))
