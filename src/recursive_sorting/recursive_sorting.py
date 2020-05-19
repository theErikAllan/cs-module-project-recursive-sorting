# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here 

    # First, we create two variables to represent our traversal through the indices of arrA and arrB
    a = 0
    b = 0

    # Next, we write a for loop that will run as many times as there are elements in the (final) merged array
    for c in range(0, elements):
        # Compare a and b
        # If a is out of range, we push b into merged array and iterate
        if a >= len(arrA):
            merged_arr[c] = arrB[b]
            b += 1
        # if b is out of range, we push a into merged array and iterate
        elif b >= len(arrB):
            merged_arr[c] = arrA[a]
            a += 1
        # if a smaller, we put it in the merged array and iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a += 1
        # if b is smaller, we put it in the merged array and iterate both
        elif arrB[b] < arrA[a]:
            merged_arr[c] = arrB[b]
            b += 1


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 : ])
        merged_arr = merge(left, right)
    return merged_arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
