# WAP to Print the Fibonacci sequence

number = int(input("Enter a number here: "))
a, b = 0, 1
if number >= 1:
    print(a)
if number >= 2:
    print(b)

for i in range(2, number):
    c = a + b
    print(c)
    a, b = b, c





# second method
number = int(input("Enter a number here: "))

# Initialize the list with the first two Fibonacci numbers
fib_sequence = [0, 1]

# Generate the Fibonacci sequence up to the specified length
for i in range(2, number):
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib)

# Handle edge cases where number is less than 2
if number == 0:
    fib_sequence = []
elif number == 1:
    fib_sequence = [0]

# Print the Fibonacci sequence
for num in fib_sequence:
    print(num)
