# First occurence 

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



# ✅ Recursively Find First and Last Index of a Target in an Array


arr = [1, 2, 3, 2, 4, 2, 5]
index = 0
first = -1
last = -1
target = 2

def firstlastidx(arr, index, first, last, target):
    if index == len(arr):
        return (first, last)
    
    if arr[index] == target:
        if first == -1:
            first = index
        last = index
    
    return firstlastidx(arr, index+1, first, last, target)

first , last = firstlastidx(arr,index , first, last, target)

print("First index:", first)
print("Last index:", last)
    
    
    

    
