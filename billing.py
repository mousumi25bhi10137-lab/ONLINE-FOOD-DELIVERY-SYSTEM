def generate_bill(cart):
    total = 0
    print("\n Your Order:")
    for item,price in cart:
        print(f"-{item} : {price}")
        total += price

    print(f"\nTotal Amount: price{total}")
    return total   

