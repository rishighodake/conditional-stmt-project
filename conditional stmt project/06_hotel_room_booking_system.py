# Hotel Room Booking System

guest_name = input("Enter guest name: ")
room_type = input(
    "Enter room type (Standard/Deluxe/Suite): "
).strip().lower()
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Invalid number of nights!")
elif room_type == "standard":
    price_per_night = 2000
elif room_type == "deluxe":
    price_per_night = 3500
elif room_type == "suite":
    price_per_night = 6000
else:
    price_per_night = 0
    print("Invalid room type!")

if nights > 0 and room_type in ("standard", "deluxe", "suite"):
    room_charge = price_per_night * nights

    if nights >= 10:
        discount_rate = 20
    elif nights >= 5:
        discount_rate = 10
    else:
        discount_rate = 0

    discount = room_charge * discount_rate / 100
    final_amount = room_charge - discount

    print("\n--- Hotel Booking Details ---")
    print("Guest Name:", guest_name)
    print("Room Type:", room_type.title())
    print("Number of Nights:", nights)
    print("Room Charge: Rs.", room_charge)
    print("Discount: Rs.", discount)
    print("Final Booking Amount: Rs.", final_amount)
