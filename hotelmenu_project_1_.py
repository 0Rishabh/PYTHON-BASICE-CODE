#  Basic Project For Hotel Menu 

menu  = {
    'pizza': 70,
    'pasta': 40,
    'burger': 60,
    'salad': 30,
    'coffee':75
}

print("...Welcome To Python Restaurent...\nHare's the menu:")
print("""Pizza  Rs70
Pasta  Rs40
Burger Rs60
Salad  Rs30
Coffee Rs75
      """)

order_total = 0

item_1 = (input("Enter the name of item you want to order: ")).lower()
#item_1 = item.lower()
if item_1 in menu:
    order_total += menu[item_1] 
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Sorry sir!..  \nOrdered item {item_1} is not available yet!")



while True:
     another_order = input("Do you want to add another item? (Yes/No) ")
     if another_order.lower() == 'yes':
         item_2 = (input("Enter the name of second item: ")).lower()
         if item_2 in menu:
             order_total += menu[item_2]
             print(f"Item {item_2} has been added to order:")
         else:
             print(f"Sorry sir!..  \nOrdered item {item_2} is not available!")
     else:
        break
     
     
print(f"The total amount of items to pay is {order_total}\nThank you Sir..")
