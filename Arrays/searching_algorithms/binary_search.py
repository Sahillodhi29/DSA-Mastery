def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = ( start + end ) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            start = mid + 1
            
        else:
            end = mid - 1
            
    return -1


arr = [2, 4, 6, 8, 10, 12]
target = 8

print(binary_search(arr, target))
    
    



# Task: Find the first occurrence of a target in a sorted array that may have duplicates.



def binary_search_first_occ(arr, target):
    start = 0
    end = len(arr) - 1
    res = -1
    
    while start <= end:
        mid = ( start + end ) // 2
        
        if arr[mid] == target:
            res = mid
            
            end = mid - 1
        
        elif arr[mid] < target:
            start = mid + 1
            
        else:
            end = mid - 1
            
    return res


arr = [2, 4, 4, 4, 6, 8]
target = 4

print(binary_search_first_occ(arr, target))



# Task: Find the last occurrence of a target in a sorted array that may have duplicates.



def binary_search_last_occurrence(arr, target):
    start = 0
    end = len(arr) - 1
    res = -1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            res = mid 
            start = mid + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return res
            

arr = [2, 4, 4, 4, 6, 8]
target = 4

print(binary_search_last_occurrence(arr, target))



# first and last both 

def first_last_occ(arr, target):
    def find_first(arr, target):
        start, end = 0, len(arr) - 1
        first = -1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                first = mid
                end = mid - 1  # move left
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return first

    def find_last(arr, target):
        start, end = 0, len(arr) - 1
        last = -1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                last = mid
                start = mid + 1  # move right
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return last

    first = find_first(arr, target)
    last = find_last(arr, target)

    return [first, last]

arr = [2, 4, 4, 4, 6, 8]
target = 4

print(first_last_occ(arr, target))
