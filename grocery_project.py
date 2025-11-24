grocery = []
total = 0

while True:
    print("1. Add Item")
    print("2. View List")
    print("3. Check Budget")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Item name: ")
        price = float(input("Price: "))
        qty = int(input("Qty: "))
        cost = price * qty

        grocery.append([name, price, qty, cost])
        total = total + cost
        print("Item Added\n")

    elif choice == 2:
        print("\nGrocery List:")
        for g in grocery:
            print(g[0], "| Price:", g[1], "| Qty:", g[2], "| Total:", g[3])
        print("Total =", total, "\n")

    elif choice == 3:
        b = float(input("Enter Budget: "))
        if total > b:
            print("You Crossed Budget by", total - b, "\n")
        else:
            print("Within Budget. Balance =", b - total, "\n")

    elif choice == 4:
    

        break

    else:
        print("Invalid Choice\n")
