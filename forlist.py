#Working with for loops on a list

numbers = [101,2,15,22,95,33,2,27,72,15,52]

for number in numbers:
    if number % 2 == 0:
        print(number)

print(sorted(numbers))

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even = even + number
    else:
        odd = odd + number
print("The sum of the even numbers is: {} ".format(even))
print('The sum of the odd numbers is: {} '.format(odd))

