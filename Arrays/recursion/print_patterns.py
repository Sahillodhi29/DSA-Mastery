# triangle

def print_triangle(n):
    if n <=0:
        return
    
    print("* "*n)
    
    print_triangle(n-1)
    
print_triangle(4)


# now reverse triangle

def reverse_triangle(n):
    if n <= 0:
        return
    reverse_triangle(n-1)
    
    print("* "*n)
    
reverse_triangle(4)

