#
# Prove 09: Assignment Milestone
#
# Author: Estefania Ortiz
#

items = []
prices = []
while True:
    print("Welcome to the Shopping Cart Program!")
    print("")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    mainmenu = input("Please enter an action: ")
    if mainmenu == "1":
        add_to_cart = input("What item would you like to add? ")
        add_price = input(f"What is the price of '{add_to_cart}'? ")
        print(f"'{add_to_cart}' has been added to the cart.")

    elif mainmenu == "2":
        print("The contents of the shopping cart are:")
        for i in range(0, len(add_to_cart)):
            print(f"{i+1}. {add_to_cart[i]} - ${add_price[i]:.2f}")
        for count, item in enumerate(add_to_cart, 1):
            for price in add_price:
                print(f'{count}. {item}', end='')                

    elif mainmenu == "3":
         item_num = int(input("Which item would you like to remove? "))
         item_num -= 1
         if item_num in range(0, len(items)):
            item = items.pop(item_num)
            prices.pop(item_num)
            print(f"'{item}' has been removed.")
         else:
             print("Sorry, that is not a valid item number.")

    elif mainmenu == "4":
        print("The total price of the items in the shopping cart is ")

    elif mainmenu == "5":
        print("Thank you. Goodbye.") 
        break
       
        
