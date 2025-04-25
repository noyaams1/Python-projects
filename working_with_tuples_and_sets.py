numbers={2,4,5,8,10}
sqrt_numbers=(4,16,25,64,100)
sorted_list = sorted(list(numbers), reverse=True)
print("Sorted list (desc):", sorted_list)
#Finding the intersection between the set and the tuple
i=0
j=0
intersection_lst=[]
for num in sorted_list:
    if num in sqrt_numbers:
        intersection_lst.append(num)

print(f"Length of the set: {len(numbers)}")
print(f"Length of the tuple: {len(sqrt_numbers)}")
#Adding a new value to the tuple (raise an error because tuples are immutable)
try:
    sqrt_numbers.append(100)  # Tuples don't have 'append'
except AttributeError as e:
    print("Error adding to tuple:", e)
print(f"Final intersection result between set and tuple: {intersection_lst}")
