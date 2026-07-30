def fibonacci(n):
    sequence = [0, 1]
    if n == 0  or n == 1:
        return sequence[n]

    res = fibonacci(n - 1) + fibonacci(n - 2)
    sequence.append(res)
    return sequence[-1]

print(fibonacci(5))
