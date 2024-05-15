# WAP convert celsius to fahrenheit 

cel = int(input("Enter the celsius: "))
F = (cel*1.8) + 32 
print("The "+ str(cel)+"° celsius is = ",F,"° fahrenheit:") 




 # Using function ( celsius to fahrenheit )
def cel_To_feh(celsius):
    return celsius*1.8 + 32

cel = int(input("Enter the celsius: "))
print("The "+ str(cel)+"° celsius is = ",cel_To_feh(cel),"° fahrenheit:") 




# WAP to convert fahrenheit to celsius 

F = float(input("Enter the Fahrenheit temperature: "))

cel = (F-32)/1.8
print("The "+ str(F)+"° fahrenheit is = ",cel,"° celsius :") 





# Using function ( fahrenheit  to celsius ) 

def feh_To_cel(fah):
    return (F-32)/1.8

F = float(input("Enter the Fahrenheit temperature: "))

print("The "+ str(F)+"° fahrenheit is = ",feh_To_cel(F),"° celsius :") 


