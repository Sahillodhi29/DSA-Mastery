arr = [10, 5, 8, 20, 15]

def second_largest(arr):
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            first , second = num , first   
        elif num != first and num > second:
            second = num 
    return second

print(second_largest(arr))