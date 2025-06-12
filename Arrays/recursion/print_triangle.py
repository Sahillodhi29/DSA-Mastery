def print_triangle(n):
    if n <=0:
        return
    
    print("* "*n)
    
    print_triangle(n-1)
    
print_triangle(4)