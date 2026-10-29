# Employee Performance Bonus

employee_name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: Rs. "))
experience = float(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-5): "))

if salary < 0 or experience < 0:
    print("Invalid salary or experience!")
elif rating < 1 or rating > 5:
    print("Invalid rating! Enter a rating from 1 to 5.")
else:
    if experience >= 10 and rating >= 4:
        bonus_percentage = 20
    elif experience >= 5 and rating >= 4:
        bonus_percentage = 15
    elif experience >= 2 and rating >= 3:
        bonus_percentage = 10
    else:
        bonus_percentage = 0

    bonus_amount = salary * bonus_percentage / 100
    final_salary = salary + bonus_amount

    print("\n--- Employee Bonus Details ---")
    print("Employee Name:", employee_name)
    print("Bonus Percentage:", bonus_percentage, "%")
    print("Bonus Amount: Rs.", round(bonus_amount, 2))
    print("Final Salary: Rs.", round(final_salary, 2))

    if rating == 5:
        print("Performance Message: Excellent Performer")
    else:
        print("Performance Message: Keep Improving")
