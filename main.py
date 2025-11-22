from login import login, create_account
from menu import take_order,show_menu
from billing import generate_bill
from delivery import delivery_status
from discount import discount
from util import confirm_order

print("WELCOME TO ONLINE FOOD DELIVERY APP")

stored_user,stored_pass = create_account()
if not login(stored_user,stored_pass):
    exit()

menu = show_menu()
cart = take_order(menu)

if len(cart) == 0:
    print("Your cart is empty. Exiting...")
    exit()   



total = generate_bill(cart) 
discount(total)


if not confirm_order():
    print("Order Cnacelled!")
    exit()
print("\n Order Confirmed! Preparing your order...") 

delivery_status()
print("\n Thank you for ordering!")

