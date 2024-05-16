
# WAP to display swap a two number 
  
 # First Method

a = int(input("Enter the value of a = :" ))
b = int(input("Enter the value of b = :" ))
c = a
a = b
b = c
print("After swapping:\n " + "a = ",a,"\n b = ",b)



        # Second Method

a1 = int(input("Enter the value of a = :" ))
b1 = int(input("Enter the value of b = :" ))
a1,b1 = b1,a1
print("After swapping:\n " + "a = ",a1,"\n b = ",b1)



# WAP to display swap a two number using function

def swap(x,y):
    temp = x
    x = y
    y = temp
    print("After swapping:\n " + "a = ",x,"\n b = ",y)

num1 = int(input("Enter the value of a = :" ))
num2 = int(input("Enter the value of b = :" ))
swap(num1,num2)

