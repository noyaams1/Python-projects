code1=str(input("Enter a word: ")).lower()
code2=str(input("Enter a word: ")).lower()
code3=str(input("Enter a word: ")).lower()
numA=int(input("Enter a number: "))
numB=int(input("Enter a number: "))
if code1.isalpha()==False or code2.isalpha()==False or code3.isalpha()==False:
    print("Invalid codeword")
    exit()
if numA < 1 or numB < 1:
    print("Invalid numbers")
    exit()

combined=code1+"-"+code2+"-"+code3
secret_number=(numA * numB) + numA - numB
numA, numB = numB, numA
swapped_A = numA
swapped_B = numB
avg_value = (swapped_A + swapped_B) / 2
message_length=len(combined)
is_palindrome = combined.replace("-", "") == combined.replace("-", "")[::-1]
print(f"Secret Code: {combined}")
print(f"Secret Number: {secret_number}")
print(f"Swapped Values: A={swapped_A}, B={swapped_B}")
print(f"Average of Originals: {avg_value}")
print(f"Combined Length: {message_length}")
print(f"Palindrome: {is_palindrome}")