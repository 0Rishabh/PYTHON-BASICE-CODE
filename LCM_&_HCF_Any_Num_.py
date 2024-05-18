
   # WAP To find any numbers LCM :-> Least common multipl

num1 = int(input("Enter number here: "))
num2 = int(input("Enter number here: "))

                               # : LCM of two numbers is always greater than those two numbers
for i in range(num1 if num1>num2 else num2 , num1*num2+1):  
    if(i%num1==0) and (i%num2==0):
        print("The least common multiple (LCM) of",num1,"And",num2,"is:",i)
        break


   # WAP to find any numbers HCF :-> The highest common factor

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for i in range(b if a>b else a ,0,-1 ):   
  
    if (a%i==0) and (b%i==0) :
        print("The highest common factor (HCF) of",a,"And",b,"is:",i)
        break
