# Basic Code


def bubble_sort(arr):
    n = len(arr)   
    
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j], arr[j+1] 
    return arr
                 
arr=[10, 2, 7, 5]

print(bubble_sort(arr))
    
    
    
    
# 🔧 Task:
# Write a function that:

# Takes an array

# Sorts it using bubble sort

# Prints the array after each pass


def bubble_sort_trace(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]
        
        print("After pass ",i+1,": ",arr)
        
arr = [10, 2, 7, 5]
bubble_sort_trace(arr)       

            
# Let’s say you're optimizing Bubble Sort.

# 💡 Challenge:
# Modify your function so that if no swaps happen in a pass, it stops early (as the array is already sorted).

# This makes it more efficient on nearly sorted arrays! 


def optimized_bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j] 
                swapped = True
        print("After pass ",i+1,": ",arr)
    
        if not swapped:
            print("arr is already sorted now!")
            break
        
                 
arr=[10, 2, 7, 5 , 6]
                    
(optimized_bubble_sort(arr))
    