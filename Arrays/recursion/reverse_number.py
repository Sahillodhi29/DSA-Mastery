def reverse_helper(n, result):
    if n == 0:
        return result
    return reverse_helper(n // 10, result * 10 + n % 10)

def reverse_number(n):
    return reverse_helper(n, 0)

# Test
print(reverse_number(1234))  # Output: 4321
print(reverse_number(100))   # Output: 1
