# Online Shopping Checkout

customer_name = input("Enter customer name: ")
purchase_amount = float(input("Enter purchase amount: "))
customer_type = input("Enter customer type (Regular/Premium): ").strip().lower()

if purchase_amount < 0:
    print("Invalid purchase amount!")
elif customer_type not in ("regular", "premium"):
    print("Invalid customer type!")
else:
    if purchase_amount >= 5000:
        discount_rate = 20
    elif purchase_amount >= 3000:
        discount_rate = 10
    elif purchase_amount >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount = purchase_amount * discount_rate / 100

    if customer_type == "premium":
        discount += purchase_amount * 5 / 100

    amount_after_discount = purchase_amount - discount

    if amount_after_discount >= 2000:
        delivery_charge = 0
    else:
        delivery_charge = 100

    final_amount = amount_after_discount + delivery_charge

    print("\n--- Shopping Checkout ---")
    print("Customer Name:", customer_name)
    print("Customer Type:", customer_type.title())
    print("Discount Amount: Rs.", round(discount, 2))
    print("Delivery Charge: Rs.", delivery_charge)
    print("Final Payable Amount: Rs.", round(final_amount, 2))
