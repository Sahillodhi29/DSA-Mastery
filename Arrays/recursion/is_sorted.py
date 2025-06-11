def is_sorted(arr, index):
    if index == 0:
        
        return True
    
    if arr[index] < arr[index-1]:
        
        return False
    
    return is_sorted(arr, index-1)


arr = [1, 2, 3, 5]
index = len(arr) - 1

if is_sorted(arr,index):
    print("Sorted")
    
else:
    print("Not Sorted")
    
    
