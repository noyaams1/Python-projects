#Answers for task 1:
'''
1.True
2.True
3.False
4.False
5.True
'''

#Answers for task 2:
'''
1.x>=10 and x<=20
2.s!="" and 'py' in s
3.n<0 or abs(n)>100
4.(user_role== "admin" and active==True) or superuser=True
5.not (temperature<0 or temperature>35)
'''

#Answers for task 3:
age=int(input("Enter your age: "))
if not(age>=0):
    print("Invalid age",)
    exit()
else:
    has_ticket=str(input("Do you have a ticket? (y/n): "))
    vip_code=str(input("Enter vip code if exists: "))
    eligible = (age>=18 and has_ticket== "y") or vip_code == "GOLDVIP"
    print(f"Access granted: {eligible}")
        
#Answers for task 4:
username = str(input("Username: "))
password = input("Password: ")
email=str(input("Email address: "))
if username!="" and len(password)>=8 and (any(char.isdigit() for char in
password)) and email.count("@") ==1 and email.endswith(".com"):
    print("Form valid")
else:
    print("Form invalid")

#Answers for task 5:
order_amount = float(input("Order amount: "))
customer_type = input("Customer type: ").lower()
coupon_code = input("Coupon code: ").upper()

surcharge = 0.05 if order_amount < 50 else 0
discount = 0.10 if customer_type in ("member", "vip") else 0
extra_discount = 0.15 if customer_type == "vip" and coupon_code == "SAVE15" else 0

order_amount += order_amount * surcharge
order_amount -= order_amount * discount
order_amount -= order_amount * extra_discount

final_payment = round(order_amount, 2)
print(f"Final total: ${final_payment}")
