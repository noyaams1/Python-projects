import math
def is_prime(num):
    if num <= 1:
        return False
    divisors = range(2, int(math.sqrt(num)) + 1)
    for i in divisors:
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(11))
print(is_prime(8))
print(is_prime(2))
