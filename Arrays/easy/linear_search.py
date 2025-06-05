# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# arr = [11, 23, 45, 9, 18]
# target = 9

# print(linear_search(arr, target))





def linear_search(arr, target):
    result = []
    
    for i in range(len(arr)):
        if arr[i] == target:
            result.append(i)
    return result   

arr = [5, 3, 7, 3, 9, 3]
target = 3

print(linear_search(arr, target))