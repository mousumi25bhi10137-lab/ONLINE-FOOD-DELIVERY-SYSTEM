def confirm_order():
    choice = input ("\n Do you want to confirm the order? (yes/no):")
    return choice.lower() == "yes"