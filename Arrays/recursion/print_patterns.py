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

# now with numbers

def print_numbers(n):
    if n<=0:
        return
    
    for i in range(1,n+1):
        print(i,end=" ")
        
    print()
    
    print_numbers(n-1)
    
print_numbers(4)



# Next pattern
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

def pattern4(n):
    if n<=0:
        return
    
    i = n
    
    while i > 0:
        print(i,end=" ")
        
        i = i-1
        
    print()  
    
    pattern4(n-1)
    
pattern4(5)



# Pattern 5

#       *
#     * *
#   * * *
# * * * *

def pattern5(n, current=1):
    if current > n:
        return 
    
    
    print("  "*(n - current), end="")  
    
    
    print("* " * current)
    
    pattern5(n, current + 1)

pattern5(4)


