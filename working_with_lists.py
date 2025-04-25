num_lst=[1,2,4,25,3,8,16,32,72,100]
num_lst.append(11)
if 5 in num_lst:
    num_lst.remove(5)
num_lst.insert(2,3)
sum_numbers=sum(num_lst)
print("Modifies list:", num_lst)
print("Sum of all numbers in the list: ", sum_numbers)
smallest_number=min(num_lst)
print("Smallest number in the list: ", smallest_number)
largest_number=max(num_lst)
print("Largest number in the list: ", largest_number)
