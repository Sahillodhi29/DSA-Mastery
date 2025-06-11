

def printnto1(n):
    if n == 0:
        return
    print(n,end=" ")
    printnto1(n-1)
    
printnto1(5)


# now 1 to n

def print1ton(n):
    if n == 0:
        return
    print1ton(n - 1)
    print(n, end=" ")  # print after the recursion

print1ton(5)

# what has happened here is , since we called the function before it could print 
# then instead of print it has to run the function first till the condition doesn't met 
# and then once it reached all conditions then he starts print them from the latest one
# to the oldest one that's how we got 1 to n



# now Sum of n 

def sumofn(n):
    if n == 0:
        return 0 
    sum = n + sumofn(n-1)
    
    return sum

print(sumofn(5))
    
    