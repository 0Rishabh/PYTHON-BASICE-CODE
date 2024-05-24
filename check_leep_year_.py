
# WAP to check leep year or not 

year = int(input("Enter a year: "))
   # Divided by 100 means century year
     # century year divided by 400 is leep year
if(year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leep year:")

    # not divided by 100 means not a century year:
       # year divided by 4 is leep year:
elif(year % 4 == 0 ) and (year % 100 !=0 ):
    print(f"{year} is leep year:")
    
      # if both are not divided means not leep year:
else:
    print(f"{year} is not a leep year:")
 
