# WAP to print to print any  number factorial 


num = int(input("Enter any number here: "))

if(num>=0):    
     s = 1
     for i in range(1,num+1):
         s = s*i
     print("Factorial of a",num , "is =",s)
  
else:
     print("The factorial of negative numbers is not defined")




# WAP to print to print any  number factorial using Fanction


def Fact(num):
     if(num>=0):
         s = 1

         for i in range(1,num+1):
              s = s*i
         print("Factorial of a",num , "is =",s)

     else:
         print("The factorial of negative numbers is not defined")

n  = int(input("Enter any number here: "))
Fact(n)





# WAP to print to print any  number factorial with help of recursion.

def fact(num):
    # Base case: if num is 0, return 1
    if num == 0:
        return 1
    else:
        # Recursive case: return num * fact(num - 1)
        return num * fact(num - 1)

n = int(input("Enter any number here: "))
r = fact(n)
print("Factorial of a",n , "is =",r)

