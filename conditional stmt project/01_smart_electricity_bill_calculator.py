# Smart Electricity Bill Calculator

customer_name = input("Enter customer name: ")
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units consumed!")
else:
    if units <= 100:
        energy_charge = units * 3
    elif units <= 200:
        energy_charge = (100 * 3) + ((units - 100) * 5)
    else:
        energy_charge = (100 * 3) + (100 * 5) + ((units - 200) * 7)

    service_charge = 150
    final_bill = energy_charge + service_charge

    print("\n--- Electricity Bill ---")
    print("Customer Name:", customer_name)
    print("Units Consumed:", units)
    print("Energy Charge: Rs.", energy_charge)
    print("Service Charge: Rs.", service_charge)
    print("Final Bill: Rs.", final_bill)

    if final_bill > 5000:
        print("Usage Message: High Usage Bill")
    else:
        print("Usage Message: Normal Usage")
