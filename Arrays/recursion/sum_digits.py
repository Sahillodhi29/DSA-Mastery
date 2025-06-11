def sum_digits(n):
    if n == 0:
        return 0
    
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))


def count_digits(n):
    
    if n<10:
        return 1
    
    return  1 + count_digits (n // 10)

print(count_digits(1234))