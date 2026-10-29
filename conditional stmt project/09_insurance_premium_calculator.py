# Insurance Premium Calculator

customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
occupation_risk = input(
    "Enter occupation risk (Low/Medium/High): "
).strip().lower()
smoker = input("Are you a smoker? (Yes/No): ").strip().lower()

base_premium = 10000

if age < 0:
    print("Invalid age!")
elif age < 18:
    print("Eligibility: Not Eligible")
    print("Reason: Customer must be at least 18 years old.")
elif occupation_risk not in ("low", "medium", "high"):
    print("Invalid occupation risk!")
elif smoker not in ("yes", "no"):
    print("Invalid smoking status!")
else:
    additional_charges = 0

    if age > 50:
        additional_charges += 5000

    if occupation_risk == "high":
        additional_charges += 7000
    elif occupation_risk == "medium":
        additional_charges += 3000

    if smoker == "yes":
        additional_charges += 5000

    final_premium = base_premium + additional_charges

    print("\n--- Insurance Premium Details ---")
    print("Customer Name:", customer_name)
    print("Eligibility: Eligible")
    print("Base Premium: Rs.", base_premium)
    print("Additional Charges: Rs.", additional_charges)
    print("Final Premium: Rs.", final_premium)

    if additional_charges >= 10000:
        print("Risk Message: High Risk Policy")
    else:
        print("Risk Message: Standard Risk Policy")
