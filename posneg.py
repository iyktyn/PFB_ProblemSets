#!/usr/local/bin/python3
num = 0

remander = num % 2

if num  == 0:
	message = 'is Zero'
elif remander == 1:
	message = 'is Odd'
else:
	message = 'is Even'
print(num , message)
