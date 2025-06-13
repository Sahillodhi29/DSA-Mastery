def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [11, 23, 45, 9, 18]
target = 9

print(linear_search(arr, target))





def linear_search(arr, target):
    result = []
    
    for i in range(len(arr)):
        if arr[i] == target:
            result.append(i)
    return result   

arr = [5, 3, 7, 3, 9, 3]
target = 3

print(linear_search(arr, target))



def count_occurence(arr,target):
    count = 0
    
    for i in range(len(arr)):
        if arr[i] == target:
            count = count+1
    return count
    
arr = [3, 5, 3, 7, 3, 1, 3]
target = 3

print(count_occurence(arr,target))