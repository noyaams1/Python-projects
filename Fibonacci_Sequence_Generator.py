def fibonacci(n):
    sequence = [0, 1, 1]
    for i in range(3, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    return sequence[:n]

print(fibonacci(35))
print(fibonacci(10))
print(fibonacci(100))

def fibonacci_list_recursive(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_list_recursive(n-1)
        seq.append(seq[-1] + seq[-2])
        return seq

print(fibonacci_list_recursive(35))
print(fibonacci(10))
print(fibonacci(100))
