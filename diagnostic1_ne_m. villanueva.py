def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping=20
    elif shipping_speed == "overnight":
        shipping=35
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping=0
    elif shipping_speed == "standard" and cart_total < 100:
        shipping=10
    else:
        print("Error. Invalid speed.")
        shipping=0
    cart_total+=shipping
    return cart_total
print(calculate_checkout(100, "express"))