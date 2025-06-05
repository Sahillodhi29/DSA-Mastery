def find_index(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1   
        
arr = [4, 7, 1, 9, 3]
target = 9
print(find_index(arr, target))  # Output: 3