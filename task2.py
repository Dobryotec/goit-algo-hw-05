def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
 
    while low <= high:
 
        mid = (high + low) // 2
        count += 1

        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return (count, arr[mid])
    if low < len(arr):
        return (count, arr[low])
    else:
        return (count, arr[high])    

    return -1

arr = [ 1.5, 2.3, 4.6, 5.1, 6.2]

print(binary_search(arr, 1.1))
print(binary_search(arr, 2.4))
print(binary_search(arr, 5.1))