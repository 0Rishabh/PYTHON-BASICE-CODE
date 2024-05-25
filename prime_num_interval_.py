
# WAP to print all prime numbers in an interval (if user choice )

s = int(input("Enter the start position: "))
e = int(input("Enter the end position: "))

print(f"The Prime number bitween {s} and {e} are:")
for i in range(s,e+1):
  if(i>1):
    
    for j in range(2,i):
        if(i%j==0):
            break
    else:
      print(i)
      
