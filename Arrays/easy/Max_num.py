arr = [10, 5, 8, 20, 7]

def max_num(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value
print(max_num(arr))  # Output: 20