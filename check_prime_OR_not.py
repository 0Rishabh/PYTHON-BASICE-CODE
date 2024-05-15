# WAP to check given number is prime OR not

 # first method #

num = int(input("Enter the number here: "))
if (num == 1):
    print("The number is not prime: ")
else:
    for i in range(2,num):
        if(num%i==0):
            print("The number is not prime: ")
            break
    else:
       print("The number is prime: ")


   # second method #

n = int(input("Enter number here: "))
if (n == 1):
    print("The number is not prime: ")

else:
         
     for i in range(2,n+1):
         if(n%i==0):
             break
     if(i==n):
         print("The number is prime number ")
     else:
     
         print("The number is not prime number ")



# Use in function to check number is prime OR not

def prime_OR_not(num):
    if(num == 1):
        print("The number is not prime:")
    else:

         for i in range(2,num):
             if(num%i==0):
                 print("The number is not prime:")
                 return
         else:
             print("The number is prime: ")
             return

n = int(input("Enter number here: "))
prime_OR_not(n)
