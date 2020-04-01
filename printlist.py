#Print a list of numbers with their lengths

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in seqs:
    print('{}\t{}'.format(len(seq),seq))
