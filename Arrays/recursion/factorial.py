# basic code

def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n*factorial(n-1)

print(factorial(5))

print(factorial(1))

print(factorial(0))


# tracing factorials

def factorial_trace(n):
    print("Entering factorial (",n,")")
    if n == 1 or n == 0:
        print("Exiting factorial ( 1 ) with result =  1")
        return 1
    
    result = n * factorial_trace(n-1)
    
    print("Exiting factorial (",n,") with result = ",result)
    
    return result

print(factorial_trace(3))
        