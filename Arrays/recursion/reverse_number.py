def reverse_number(n):
    if n == 0:
        return
    print(n % 10, end="") 
    reverse_number(n//10)
reverse_number(1234)