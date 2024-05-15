# WAP to print number is Even or odd

n = int(input("Enter any number here: "))
if(n%2==0):
   print("Given number is Even number:")
else:
    print("Give number is Not Odd number")





#  Use in function to check number is even OR odd 

def even_odd(n):
  if(n%2==0):
    print("Given number is even ")
  else:
    print("Given number is odd ")
num = int(input("Enter any number here: ")) 
even_odd(num)
