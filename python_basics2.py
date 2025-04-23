'''Exercise 1: Salary Breakdown'''
gross_salary = float(input("Enter your gross monthly salary: "))
tax_rate = 0.22
net_salary = gross_salary * (1 - tax_rate)
rent=3000
savings=1000

if net_salary - rent >=  savings:
    print("Rent and save!")
elif net_salary >= rent:
    print("Just rent")
else:
    print("Not enough")

'''Exercise 2: Shipping Calculator'''
item_price=float(input("Enter the item's price: "))
quantity=int(input("Enter the quantity of your item: "))
total_cost = item_price * quantity
shipping_fee = 0 if total_cost > 200 else 20
if total_cost > 500:
    print("You've got a discount of 10% off your order")
    total_cost *= 0.90

if shipping_fee > 0:
    print("Shipping fee added: $20")
total_cost += shipping_fee
print(f"Your order's total cost is: ${total_cost:.2f}")

'''Exercise 3: Medieval Guard Duty'''
age=int(input("Visitor's age:  "))
has_gold_pass=input("Does the visitor has gold pass? (y/n): ").lower() == 'y'
is_royal_family=input("Does the visitor part of the royal family? (y/n): ").lower() == 'y'
is_blacklisted=input("Is the visitor's on the black list? (y/n): ").lower() == 'y'

if age >= 18 and (has_gold_pass or is_royal_family) and not is_blacklisted:
    print("Visitor's allowed in")
else:
    print("Visitor's not allowed in")

'''Exercise 4: Car Insurance Quote'''
driver_age=int(input("Driver's age:  "))
accident_count=int(input("Number of past accidents: "))
if age < 25:
    premium=3000
else:
    premium=2000
damage_cost= accident_count * 500
insurance_cost= premium+damage_cost
if insurance_cost > 5000:
    risk_level="High Risk"
else:
    risk_level="Standard"
print(f"Premium package: ${premium}")
print(f"Damage cost: ${damage_cost}")
print(f"Insurance's cost is: ${insurance_cost}")
print(f"Risk level: {risk_level}")

'''Exercise 5: Lab Safety Checklist'''
temperature=float(input("Temperaure: "))
pressure=int(input("Pressure: "))
voltage=int(input("Voltage: "))
if 20 < temperature < 80 and pressure < 50 and 200 < voltage < 250:
    print("Safe to proceed")
else:
    print("Unsafe conditions")

'''Exercise 6: Wizard’s Final Exam'''
spell_power=int(input("Spell power (0-100): "))
accuracy=int(input("Accuracy (0-100): "))
control=int(input("Control (0-100): "))
if spell_power < 40 or accuracy < 40 or control < 40:
    print("Fail")
else:
    average_score=(accuracy+control)/2
    if average_score >=90:
        print("Archmage")
    elif 75 <= average_score <90:
        print("Mage")
    elif 60 <= average_score <75:
        print("Apprentice")
    else:
        print("Fail")


