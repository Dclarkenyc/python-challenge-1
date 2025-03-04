# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = {}

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1


            # 2. Ask customer to input menu item number
            item_number = input("Please let me know what item number you want? ")    

            # 3. Check if the customer typed a number
            
            if item_number.isdigit(): 
                # Convert the menu selection to an integer 

                item_number = int(item_number)
                # Check if the customer's input is a valid option   
                
                # 4. Check if the menu selection is in the menu items

                if int(item_number) in menu_items.keys():
        
                # Store the item name as a variable

                    item = menu_items[item_number]
    
            
                    # Ask the customer for the quantity of the menu item
                    item_quanitity = input(f"How many {item["Item name"]}s do you want? ")

                # Check if the quantity is a number, default to 1 if not
                    if item_quantity. isdigit():
                        item_quantity = int(item_quantity)
                    else:
                        item_quantity = int(1)
                
                # Add the item name, price, and quantity to the order list     
                        item = menu_items[item, menu_items[value], item_quantity]       
    #   how does this add the order list - did we make an order list - WHY NOT 
                           
           
             # Tell the customer that their input isn't valid
            else: 
                print("Your input is not valid.")                

                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} is not a menu option.")
   
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

        if keep_ordering = upper(Y):
             

                # Keep ordering


                # Exit the keep ordering question loop

        
            break
# NOT sure if above is correct way to end this
                # Complete the order ???????????

# NOT SURE how to go back to the start of a while loop
                
                # Since the customer decided to stop ordering, thank them for
                # their order
            print("Thank you for your order")
                # Exit the keep ordering question loop
# ?

                # Tell the customer to try again
        else:
            "Sorry we are looking for a Y for Yes and an N for No - try again"
# Not sure how to start and stop loops - 


        # Print out the customer's order
print("This is what we are preparing for you.\n")

    

         # Uncomment the following line to check the structure of the order
        #print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

 for key, value in menu_items[key]():


    # 7. Store the dictionary items as variables
#  How do I do that?

    # 8. Calculate the number of spaces for formatted printing
    # 9. Create space strings
 for item in menu_items():
            item_spaces1A = 26 - len(key + key2) -3
            item_spaces1 = " " * item_spaces1A
            item_spaces2A = 8 - len(value2)
                if item_spaces2A > 9.99 and < 100.00
                        item_spaces2 = (" " * 3)     
                    if item_spaces2A > 99.99 
                        item_spaces2 = (" " * 2)
                    else:
                        item_spaces2 = (" " * 5)
                       item_spaces3A =  10 - len(item_quantity)
                if item_spaces3A > 9
                     item_spaces3 = (" " * item_spaces2A)-1
                    else:  
                        item_spaces3 = (" " * item_spaces1A)

#10. Print the item name, price, and quantity - do I need to tell it to print the menu items dictionary below?

             print(f"{key} - {key2}{item_spaces1}|({item_spaces2}${value2}   |{item_space3}{item_quantity}")
    # 11. Calculate the cost of the order using list comprehension

print(f"Total order cost: ${sum(menu_items[value] * item_quantity)}")

# Multiply the price by quantity for each item in the order list, then sum()

for items in menu_items

price_items = menu_items[value] * [item_quantity]


# and print the prices.


Print [price_items]





# LIST comprehension

