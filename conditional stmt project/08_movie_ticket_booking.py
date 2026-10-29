# Movie Ticket Booking

customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
show_type = input("Enter show type (Morning/Evening): ").strip().lower()
day_type = input("Enter day type (Weekday/Weekend): ").strip().lower()

base_price = 200

if age < 0:
    print("Invalid age!")
elif show_type not in ("morning", "evening"):
    print("Invalid show type!")
elif day_type not in ("weekday", "weekend"):
    print("Invalid day type!")
else:
    if age < 12:
        discount = base_price * 50 / 100
    elif age >= 60:
        discount = base_price * 30 / 100
    else:
        discount = 0

    if show_type == "morning":
        discount += 30

    if day_type == "weekend":
        surcharge = 50
    else:
        surcharge = 0

    final_price = base_price - discount + surcharge

    print("\n--- Movie Ticket Details ---")
    print("Customer Name:", customer_name)
    print("Original Ticket Price: Rs.", base_price)
    print("Total Discount: Rs.", discount)
    print("Weekend Surcharge: Rs.", surcharge)
    print("Final Ticket Price: Rs.", final_price)
