
# Write a Python Program for cube sum of first n natural numbers?

def cube_sum_of_natural_numbers(n):
    if n <= 0 :
        return 0
    else:
        result = 0
        for i in range(1,n+1):
            result+= i**3
    return result


# Input the number of natural numbers
n = int(input("Enter the value of n: "))

if n <= 0:
 print("Please enter a positive integer.")

else:
 result = cube_sum_of_natural_numbers(n)
 print(f"The cube sum of the first {n} natural numbers is: {result}")
