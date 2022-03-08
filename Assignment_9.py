# check is it a prime number
number = int(input("Please enter a whole number: "))
counter = 0 # ==> 2

for i in range(1, number+1):
    if number % i == 0:
        counter += 1

if (number == 0) or (number == 1) or (counter > 2):
    print(f'The number {number} is not a prime number')
else:
    print(f'The number {number} is a prime number')