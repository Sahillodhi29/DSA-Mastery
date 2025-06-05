arr = [4, 7, 2, 8, 9, 10]

def count_even(arr):
    count=0
    
    for i in arr:
        if i%2 == 0:
            count=count+1
    return count
            

print(count_even(arr))