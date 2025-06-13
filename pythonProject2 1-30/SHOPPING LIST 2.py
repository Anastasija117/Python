shopping_list = []
prices = []

while True:
    item = input("Enter an item on your shopping list(q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of an {item}: "))
        shopping_list.append(item)
print("-----YOUR SHOPPING LIST-----")
for item in shopping_list:
    print(item.capitalize(), end=" ")