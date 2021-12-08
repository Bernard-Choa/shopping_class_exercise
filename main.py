def fancy_food_list():
    items_ordered = int(input("How many items will you order today? "))
    while items_ordered < 1:
        print("Number of items must be at least 1.")
        items_ordered = int(input("How many items will you order today? "))
    list_of_orders = []
    for i in range(items_ordered):
        print(f"Item #{i+1}-")
        name_of_food = input("Enter food: ")
        amount_ordered = float(input("Enter amount of pounds: "))
        while amount_ordered <= 0:
            print("Amount of pounds must be greater than 0.")
            amount_ordered = float(input("Enter amount of pounds: "))
        item = FancyFood(name_of_food, amount_ordered)
        print("")
        list_of_orders.append(item)
    return list_of_orders


def fancy_food_display(list_of_orders):
    print("Here's a summary of the items purchased:")
    print("---------------------------------")
    for i in range(len(list_of_orders)):
        list_of_orders[i].food_cost()
        print(f"Item: {list_of_orders[i].type}")
        print(f"Amount ordered: {list_of_orders[i].weight} pounds")
        print(f"Price per pound: ${list_of_orders[i].get_standard_price():.2f}")
        print(f"Price of order: ${list_of_orders[i].food_cost():.2f}")
        print("")


def total_cost_calc(list_of_orders):
    total_cost = 0
    for i in range(len(list_of_orders)):
        total_cost += list_of_orders[i].food_cost()
    return total_cost


def mainFancyFood():
    de_listo = fancy_food_list()
    fancy_food_display(de_listo)
    print(f"Total cost: ${total_cost_calc(de_listo):.2f}")


mainFancyFood()
