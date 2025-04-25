start = int(input("Enter a start number for range: "))
end = int(input("Enter an end number for range: "))
divisor = int(input("Enter a divisor: "))

# Using For loop
divisible_numbers_for = []
print("\nUsing for loop:")
for num in range(start, end + 1):
    if num % divisor == 0:
        divisible_numbers_for.append(num)
        print(num)
print(f"Total count (for loop): {len(divisible_numbers_for)}")

# Using While loop
divisible_numbers_while = []
print("\nUsing while loop:")
num = start
while num <= end:
    if num % divisor == 0:
        divisible_numbers_while.append(num)
        print(num)
    num += 1
print(f"Total count (while loop): {len(divisible_numbers_while)}")
