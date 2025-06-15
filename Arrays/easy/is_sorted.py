arr1 = [2, 4, 7, 10]



def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

   
print(is_sorted(arr1))