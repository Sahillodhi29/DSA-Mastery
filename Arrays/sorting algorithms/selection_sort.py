# Basic Code

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i],arr[min_index]=arr[min_index],arr[i]   
        
        print("After pass", i + 1, ":", arr)


arr=[7, 4, 10, 8, 3, 1]

selection_sort(arr)