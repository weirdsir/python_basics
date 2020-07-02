user_count = int(input("Enter a number of goods: "))
max_count = 0
i = 0
list = []
while max_count != user_count:
    name = input("Enter your good's name: ")
    price = int(input("Enter good's price: "))
    quantity = int(input("Enter quantity: "))
    unit = input("Enter a unit to measure your goods: ")
    items = (i + 1, {"Name ": name, "Price ": price, "Quantity ": quantity, "Unit ": unit})
    list.append(items)
    max_count += 1
    i += 1
print(list)
