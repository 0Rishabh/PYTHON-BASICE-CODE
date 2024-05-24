
# WAP to print calendar 

import calendar
y = int(input("Enter Year: "))
m = int(input("Enter Month: "))
calendar = calendar.month(y,m)
print(calendar)
