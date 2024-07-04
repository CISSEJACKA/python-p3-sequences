# sequences.py

def print_fibonacci(length):
    fibonacci_list = []
    if length > 0:
        a, b = 0, 1
        for _ in range(length):
            fibonacci_list.append(a)
            a, b = b, a + b
    print(fibonacci_list)

