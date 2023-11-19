
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range( n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[ j +1] = arr[ j +1], arr[j]
    return arr



arr = [2 ,7, 1, 4, 10]

print("before sorting", arr)

arr = bubble_sort(arr)

print("after sorting ", arr)
