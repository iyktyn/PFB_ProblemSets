import sys

dna = sys.argv[1]
dna = dna.upper()

dna_len = len(dna)

a_count = dna.count('A')
t_count = dna.count('T')
c_count = dna.count('C')
g_count = dna.count('G')

AT_count = a_count + t_count
GC_count = g_count + c_count

AT_content = AT_count / dna_len
GC_content = GC_count / dna_len

print('Your AT content is {:%} and your GC content is {:%}'.format(AT_content, GC_content))
