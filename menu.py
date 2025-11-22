def show_menu():
    menu = {
        1: ("PIZZA", 150),
        2: ("BURGER", 80),
        3: ("PASTA", 120),
        4: ("SANDWICH", 60),
        5: ("COLD COFFEE", 90),
        6: ("MOMOS", 100),
        7: ("MOCHA", 90),
        8: ("FRIES", 80)
    }

    print("----------------------------------")
    print("FOOD  MENU    |    PRICE          ")
    print("----------------------------------")
    for item, (name, price) in menu.items():
        print(f"{item}. {name}  |  {price}")

    return menu



def take_order(menu):
    cart = []
    choices = input("Enter item numbers separated by commas (e.g., 1,3,5): ").strip()
    if not choices:
        print("No items selected. Your cart is empty.")
        return cart

    for choice_str in choices.split(","):
        choice_str = choice_str.strip()
        if not choice_str.isdigit():
            print(f"Invalid entry: {choice_str}")
            continue
        choice = int(choice_str)
        if choice in menu:
            item_name, price = menu[choice]
            cart.append((item_name, price))
            print(f"Added {item_name} to cart.")
        else:
            print(f"Invalid item number: {choice}")
    return cart