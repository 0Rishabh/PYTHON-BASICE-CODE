# WAP to check a number is Armstrong number OR not
num = int(input("Enter a number here: "))
d = 0
x = num
o = len(str(x))

while x > 0:
    s = x % 10
    d += s ** o
    x //= 10

if d == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
