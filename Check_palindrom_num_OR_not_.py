# WAP to check the number is palindrome number OR not

num = int(input("Enter a number here: "))

d = 0
x = num

while x > 0:
    s = x % 10
    d = d*10 + s
    x //= 10

if(d==num):
    print(f"{num} is palindrome number")

else:
    print(f"{num} is not palindrome number")



# WAP to check the number is palindrome number OR not
     # using the string method
number= int(input("Enter a number here: "))

      # Convert the number to a string
str_convert = str(number)

         # Reverse the string             
reversed = int(str_convert[::-1]) # Convert the reversed string back to an integer.

if(reversed==number): # check intput number is equal to the revers number
     print(f"{number} is palindrome number")
else:
  print(f"{number} is not palindrome number")
