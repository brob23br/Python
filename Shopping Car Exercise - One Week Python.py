'''Write a Python script that does the following:
Prints out a “banner” to welcome users to our shop
Asks the user for the name of the item they are buying
Asks the user for the price of that item
Asks the user for the quantity they are purchasing
Prints out a message that includes their subtotal (quantity 𝚡 price)'''

print("Welcome to our shop of random shit!")

item = input("What is the name of the item that you want to buy?")
price = input(f"What is the price of the {item}?")
quantity = input(f"How many {item} would you like to buy?")

print(f"Added {quantity} {item}(s) to shopping cart.\nSubtotal: ${float(quantity) * float(price)}")
