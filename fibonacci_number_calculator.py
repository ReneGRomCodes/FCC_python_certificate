def fibonacci(n):
    """Find and nth fibonacci number without using recursion."""
    sequence = [0, 1]

    if n == 0: return 0

    for i in range(n-1):
        sequence[0], sequence[1] = sequence[1], sequence[0] + sequence[1]

    return sequence[1]


# Test cases.
print(fibonacci(0))     # Should return 0
print(fibonacci(1))     # Should return 1
print(fibonacci(2))     # Should return 1
print(fibonacci(3))     # Should return 2
print(fibonacci(5))     # Should return 5
print(fibonacci(10))    # Should return 55
print(fibonacci(15))    # Should return 610
