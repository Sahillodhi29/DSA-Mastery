arr = [1, 2, 3, 4, 5]

# [5, 4, 3, 2, 1] output

def reverse_array(arr):
    
    start=0
    end=len(arr)-1
    
    while start < end :
        arr[start] , arr[end] = arr[end] , arr[start]  # ese hota hai swap aage se yaad rakhna
        
        start=start+1
        end=end-1
    return arr

print(reverse_array(arr))
    
