#Print range of numbers between the input values

import sys

low = int(sys.argv[1])
high = int(sys.argv[2]) + 1

for number in range(low,high):
    print(number)
