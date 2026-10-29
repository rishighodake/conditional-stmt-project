# ATM Withdrawal System

account_holder = input("Enter account holder name: ")
balance = float(input("Enter current balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

print("\n--- ATM Transaction ---")
print("Account Holder:", account_holder)

if balance < 0:
    print("Transaction Status: Invalid account balance")
elif withdrawal <= 0:
    print("Transaction Status: Invalid withdrawal amount")
    print("Reason: Amount must be greater than Rs. 0")
elif withdrawal > 20000:
    print("Transaction Status: Rejected")
    print("Reason: Maximum withdrawal is Rs. 20,000")
elif withdrawal > balance:
    print("Transaction Status: Rejected")
    print("Reason: Insufficient balance")
else:
    remaining_balance = balance - withdrawal

    print("Transaction Status: Successful")
    print("Withdrawn Amount: Rs.", withdrawal)
    print("Remaining Balance: Rs.", remaining_balance)

    if remaining_balance < 1000:
        print("Warning: Low Balance Warning")
