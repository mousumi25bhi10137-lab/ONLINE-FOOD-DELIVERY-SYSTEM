def discount(total):
    discount = 0
    if total >= 500:
        discount = total * 0.10
        print(f"10% discount applied: -{discount:.2f}")
    elif total >=300:
        discount = total * 0.05
        print(f"5% discount applied: -{discount:.2f}")
    final_amount = total-discount
    print(f"Final Amount to pay:{final_amount:.2f}")  
    print("------------------------------------------------")      
    print("\n ORDER CONFIRMED! Thank you for ordering")