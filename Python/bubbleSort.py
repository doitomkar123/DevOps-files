def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [8, 1,34, 434, 65,66, 7,8,0]
print(bubblesort(arr))
# Big O(n^2)