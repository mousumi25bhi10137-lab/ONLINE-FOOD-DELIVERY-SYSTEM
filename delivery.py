import time 
def delivery_status():
    print("\nDelivery Status:")
    stages = [
        "Order Received",
        "Restaurant is preparing your food",
        "Order picked up by delivery partner",
        "Delivered!"
    ]
    for stage in stages:
        print(stage)
        time.sleep(1)