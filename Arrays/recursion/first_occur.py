arr = [1, 2, 3, 4, 2, 5]
index= 0
target = 2

def first_occur(arr, index, target):
    if arr[index] == len(arr):
        return -1 
    if arr[index] == target:
        return index
    
    return first_occur(arr, index+1, target)

print(first_occur(arr, index, target))