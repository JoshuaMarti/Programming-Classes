#Initialize Things
entry = ""
cart = []
quantity = []
prices = []
print("Welcome to the Shopping Cart Program\nType \"Quit\" to quit\n")
#Master Loop
while entry != "Quit":
    print("\nPlease select from the following\n1: Add item\n2: View cart")
    print("3: Remove Item\n4: Calculate total\n5: Export list")
    entry = input("Enter your selection: ").title()
    if entry == "1":
        newItem = input("Item: ").title()
        newQuantity = int(input("Quantity: "))
        newPrice = float(input("Price: $"))
        if newItem in cart:
            comparisonToIndex = cart.index(newItem)
            if newPrice == prices[comparisonToIndex]:
                quantity[comparisonToIndex] = quantity[comparisonToIndex] + newQuantity
            else:
                print(f"{quantity[comparisonToIndex]} of {newItem} is already in your cart for ${prices[comparisonToIndex]}")
                print("Would you like to replace that entry? Y/N")
                replace = input("   ").title()
                while replace != "Y" and replace != "N":
                    print("Would you like to replace that entry? Y/N")
                    replace = input("   ").title()
                if replace == "N":
                    print("New item not added. Previous entry remains.")
                elif replace == "Y":
                    print(f"Replacing {quantity[comparisonToIndex]} of {cart[comparisonToIndex]} for ${prices[comparisonToIndex]} with {newQuantity} of {newItem} for ${newPrice}")
                    cart[comparisonToIndex] = newItem
                    quantity[comparisonToIndex] = newQuantity
                    prices[comparisonToIndex] = newPrice
                else:
                    print("Error Code 0910.35")
        else:
            cart.append(newItem)
            quantity.append(newQuantity)
            prices.append(newPrice)
    #View Cart
    if entry == "2":
        for spot in range(len(cart)):
            print(f"{spot+1}: {quantity[spot]} of {cart[spot]} at ${prices[spot]}")
    #Remove Item
    if entry == "3":
        print("1: Remove by Number\n2: Remove by Name")
        removalMethod = input("Choose 1 or 2: ")
        while removalMethod != "1" and removalMethod != "2":
            print("1: Remove by Number\n2: Remove by Name")
            removalMethod = input("Choose 1 or 2: ")
        if removalMethod == "1":
            removeIndex = int(input("Select Item Number: ")) - 1
            while removeIndex > len(cart) and removeIndex != "exit":
                print(f"Out of bounds. Try again or type \"exit\"")
                removeIndex = input("Select Item Number: ").lower()
                if removeIndex != "exit":
                    removeIndex = int(removeIndex) - 1
            if removeIndex != "exit":
                del cart [removeIndex]
                del quantity [removeIndex]
                del prices [removeIndex]
        elif removalMethod == "2":
            removeItem = input("Item Name: ").title()
            while removeItem not in cart and removeItem != "Exit":
                print(f"{removeItem} is not in your cart. Try again or type \"exit\"")
                removeItem = input("Item Name: ").title()
            if removeItem != "Exit":
                removeIndex = cart.index(removeItem)
                del cart [removeIndex]
                del quantity [removeIndex]
                del prices [removeIndex]
    #Calculate Total
    if entry == "4":
        totalCost = 0
        for spot in range(len(prices)):
            totalCost = totalCost + prices[spot] * quantity[spot]
        print(f"The total cost is ${totalCost} for the {len(cart)} unique items in your cart.")
    if entry == "5":
        print("Preparing to export your Shopping Cart")
        totalCost = 0
        for spot in range(len(prices)):
            totalCost = totalCost + prices[spot] * quantity[spot]
        fileName = input("Enter desired File Name: ")
        completeFileName = fileName+".txt"
        with open(completeFileName, "a") as outputFile:
            for spot in range(len(cart)):
                print(f"{spot+1}: {quantity[spot]} of {cart[spot]} at ${prices[spot]}", file = outputFile)
            print(f"Total cost: ${totalCost} for {len(cart)} unique items.", file = outputFile)
        print(f"Your Shopping Cart has been appended to {completeFileName}")
    