#   Write a Python Program to Make a Simple Calculator 
        # with 4 basic mathematical operations

  # This function add two numbers
def add(x,y):
   return x + y

  # This function subtracts two numbers
def subtract(x , y):
    return x - y 

  # This function multiplies two numbers
def multiply(x , y):
    return x * y

  # This function divides two numbers
def divide(x , y):
    return x / y


print("""
      Select Operation.
      1. Add
      2. Subtract
      3. Multiply
      4. Divide
      """)

while True:
    
       # Take input from the user
       choice = input("Enter your Choice(1/2/3/4): ")

       # Check if choice is one of the four options:
       if choice in ('1' , '2' , '3' , '4'):
            try:
                 num1 = float(input("Enter First Number: "))
                 num2 = float(input("Enter Second Number: "))
            except ValueError:
                 print("Invalid input. Please Enter a number. ")
                 continue
            
            if choice == '1':
                 print(f"{num1} + {num2} = {add(num1,num2)}")

            elif choice == '2':
                 print(f"{num1} - {num2} = {subtract(num1,num2)}")

            elif choice == '3':
                 print(f"{num1} x {num2} = {multiply(num1,num2)}")

            elif choice == '4':
                 print(f"{num1} / {num2} = {divide(num1,num2)}")


      # check if user wants another calculation
             # break the while loop if answer is no
            next_calculation = input("Let's do next calculation..? (yes/no):")
            
            if next_calculation.lower() == "no":
                 break
            
       else:
            print("Invalid Input:")  
        
