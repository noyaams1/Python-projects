print("Welcome to Movie Night Ticket Calculator")
age=int(input("Age? "))
day=str(input("Day (weekday/weekend)? ")).lower()
is_loyalty_member=str(input("Loyalty member (y/n)? ")).lower()
if age < 0:
    print("Invalid age")
    exit()

if day != "weekday" and day != "weekend":
    print("Invalid day")
    exit()

price = 20
if age < 13:
    price *= 0.5
elif age >= 60:
    price *= 0.7

if day == "weekend":
    price += 5
if is_loyalty_member == "y":
    price -= 2

print(f"Total: ${int(price)}")