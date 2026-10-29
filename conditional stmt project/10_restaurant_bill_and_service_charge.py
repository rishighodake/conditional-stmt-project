# Restaurant Bill and Service Charge

customer_name = input("Enter customer name: ")
food_bill = float(input("Enter food bill amount: Rs. "))
membership = input("Are you a member? (Yes/No): ").strip().lower()

if food_bill < 0:
    print("Invalid bill amount!")
elif membership not in ("yes", "no"):
    print("Invalid membership status!")
else:
    if food_bill >= 5000:
        discount_rate = 15
    elif food_bill >= 3000:
        discount_rate = 10
    elif food_bill >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount = food_bill * discount_rate / 100

    if membership == "yes":
        discount += food_bill * 5 / 100

    amount_after_discount = food_bill - discount
    service_charge = amount_after_discount * 5 / 100
    final_amount = amount_after_discount + service_charge

    print("\n--- Restaurant Bill ---")
    print("Customer Name:", customer_name)
    print("Original Bill: Rs.", food_bill)
    print("Total Discount: Rs.", round(discount, 2))
    print("Service Charge: Rs.", round(service_charge, 2))
    print("Final Payable Amount: Rs.", round(final_amount, 2))

    if final_amount >= 5000:
        print("Thank you for being a valued customer")
    else:
        print("Thank you for visiting us!")
