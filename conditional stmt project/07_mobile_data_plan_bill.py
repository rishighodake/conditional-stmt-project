# Mobile Data Plan Bill

customer_name = input("Enter customer name: ")
plan_type = input(
    "Enter plan type (Basic/Standard/Premium): "
).strip().lower()
extra_data = float(input("Enter extra data used in GB: "))

if extra_data < 0:
    print("Invalid data usage!")
elif plan_type == "basic":
    base_charge = 299
elif plan_type == "standard":
    base_charge = 499
elif plan_type == "premium":
    base_charge = 799
else:
    base_charge = 0
    print("Invalid plan type!")

if extra_data >= 0 and plan_type in ("basic", "standard", "premium"):
    extra_data_charge = extra_data * 20

    if extra_data > 10:
        surcharge = 100
    else:
        surcharge = 0

    final_bill = base_charge + extra_data_charge + surcharge

    print("\n--- Mobile Data Bill ---")
    print("Customer Name:", customer_name)
    print("Plan Type:", plan_type.title())
    print("Base Plan Charge: Rs.", base_charge)
    print("Extra Data Charge: Rs.", extra_data_charge)
    print("Surcharge: Rs.", surcharge)
    print("Final Bill: Rs.", round(final_bill, 2))
