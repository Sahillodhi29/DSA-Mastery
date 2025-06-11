arr = [1, 2, 3, 2, 4, 2, 5]
index = 0
target = 2

def printindices(arr, index, target):
    
    if index >= len(arr):
        return 
    
    if arr[index] == target:
        print(target," found at index: ",index)
        
    printindices(arr, index+1, target)


printindices(arr, index, target)