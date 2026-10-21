def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping_bill = 20
    elif shipping_speed == "overnight":
        shipping_bill = 35
    elif shipping_speed == "standard" and cart_total <= 100:
        shipping_bill = 0
    elif shipping_speed == "standard" and cart_total > 100:
        shipping_bill = 10 
    else:
        print("Error. Not an option.")
        shipping_bill = 0
    
    final_bill = shipping_bill + cart_total
    return final_bill
print(calculate_checkout(1000, "express"))
