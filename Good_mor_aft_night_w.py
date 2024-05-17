# WAP To print current time and wish the Messages
import time
    
hours = time.strftime('%H')

if (11>=int(hours)):
        print("Good Morning")

elif (11 < int(hours) and 18 > int(hours)):
                 print("Good Afternoon")

elif( 17 < int(hours) and 19>int(hours)):
            print("Good Evening")
else:
        print("Good night")


# current time print 
while True:
    c = time.ctime()

    print("Current Time:", c , end="\r")
    
    time.sleep(1)
