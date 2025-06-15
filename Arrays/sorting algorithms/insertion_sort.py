# Basic Code

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1,n):
        key = arr[i]
        
        j = i-1
        
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            
            j=j-1
        
        arr[j+1]=key
        
        print("After pass", i, ":", arr)
        
        
        

arr = [8, 4, 1, 5]
insertion_sort(arr)






# 🧪 Problem 1: Sort an Array in Descending Order Using Insertion Sort
# ✏️ Modify the insertion sort logic to sort in descending order.

arr = [8, 4, 1, 5]
def desc_sort(arr):
    n = len(arr)
    
    for i in range(1,n):
        key = arr[i]
        
        j = i-1
        
        while j>=0 and arr[j]<key:
            arr[j+1]=arr[j]
            
            j = j-1
        
        arr[j+1] = key
        
        print("after pass",i,":",arr)
        
desc_sort(arr)



# 🧪 Problem 2: Count Total Shifts During Insertion Sort
# Every time you shift an element to the right (arr[j+1] = arr[j]), count it.


def shift_count(arr):
    n = len(arr)
    count = 0
    for i in range(1,n):
        key = arr[i]
        
        j = i - 1
        
        while j >=0 and arr[j]>key:
            
            arr[j+1]=arr[j]
            
            count=count+1
            
            j=j-1
            
            
        arr[j+1] = key    
        print("after pass",i,":",arr)
 
    return count
   
arr=[4, 3, 2, 1] 
      
print(shift_count(arr))
        


    