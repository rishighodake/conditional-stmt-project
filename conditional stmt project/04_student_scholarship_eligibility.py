# Student Scholarship Eligibility

student_name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
family_income = float(input("Enter annual family income: Rs. "))
attendance = float(input("Enter attendance percentage: "))

print("\n--- Scholarship Eligibility ---")
print("Student Name:", student_name)

if not (0 <= percentage <= 100 and
        family_income >= 0 and
        0 <= attendance <= 100):
    print("Eligibility Status: Invalid Input")
    print("Please enter valid marks, income, and attendance.")
elif (percentage >= 75 and
      family_income <= 400000 and
      attendance >= 75):

    print("Eligibility Status: Eligible")

    if percentage >= 90:
        print("Scholarship Category: Full Scholarship")
    else:
        print("Scholarship Category: Partial Scholarship")

else:
    print("Eligibility Status: Not Eligible")
    print("Reason:")

    if percentage < 75:
        print("- Percentage is below 75%")

    if family_income > 400000:
        print("- Annual family income exceeds Rs. 4,00,000")

    if attendance < 75:
        print("- Attendance is below 75%")
