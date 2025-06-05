
arr = [1, 3, 2, 3, 4, 1, 5 , 5, 5 , 6]


def remove_duplicates(arr):
    seen = set()
    
    result= []
    
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result

print(remove_duplicates(arr))