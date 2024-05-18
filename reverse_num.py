
  # WAP to print reverse of a number 
num = int(input("Enter number here: "))
x = num 
order = len(str(x))
d=0
while(x>0):
    s = x%10
    d = (d*10)+s
    x = x//10
print("Reverse of a number: ",d)


# WAP to print reverse a number by using Function :
def Rev(x,d=0):
      order = len(str(x))
      while(x>0):
           s = x%10
           d = (d*10)+s
           x = x//10
      print("Reverse of a number:",d)

num = int(input("Enter number here: "))
Rev(num)




   # Function to reverse a number : Using string method.

def rev_num(n):
         # Convert the number to a string
    str_num = str(n)
                # Reverse the string
    rev_str = str_num[::-1]
         # Convert the reversed string back to an integer
    rev_num = int(rev_str)
    return rev_num


num = int(input("Enter a number: "))
print("Reversed number:",rev_num(num))
