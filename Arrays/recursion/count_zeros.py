def count_zeros(n):
    
    if n == 0:
        return 1
    
    def helper(n):
        if n == 0:
            return 0
        
        return (1 if n % 10 == 0 else 0) + helper(n//10)
    
    return helper(n)

    
    

print(count_zeros(5050001))