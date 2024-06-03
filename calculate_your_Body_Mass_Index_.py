        
          
#   Write a Python Program to calculate your Body Mass Index.
    #   Formula :>   BMI = Weight(kg) / Height(m)^2


def bodymassindex(height , weight):
    return round((weight / height**2),2)

 #     Body Mass Index (BMI) is a measure of body fat based 
   #            on an individual's weight and height


h = float(input("Enter your height in meters : "))
w = float(input("Enter your weight in Kg: "))

print("Welcome to the BMI calculator:")
BMI = bodymassindex(h , w)
print("Your body mass index is ",BMI)
          
if BMI <= 18.5:
 print("You are underweight.")

elif 18.5 < BMI <= 24.9:
 print("Your weight is normal.")

elif 25 < BMI <= 29.29:
 print("You are overweight.")
 
else:
 print("You are obese.")
          
