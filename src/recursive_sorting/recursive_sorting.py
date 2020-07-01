# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here 

    # First, we create two variables to represent our traversal through the indices of arrA and arrB
    a = 0 #arrA index
    b = 0 #arrB index

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
    # First, we set a conditional statement for our base case
    # If the array is larger than 1 element, we want to split it up
    if len(arr) > 1:
        # We set a variable to the middle index of the array so we know where to split it
        middle = len(arr) // 2
        # Then we recursively call the merge_sort() function on the "left" side of the array, assuming the left side starts with index 0 and goes up to the middle index that we already determined
        left = merge_sort(arr[0 : middle])
        # We also do the same for the "right" side of the array
        right = merge_sort(arr[middle : ])
        # Next, we call the helper function merge() and pass in the left and right sides of the array to be sorted and merged
        merged_arr = merge(left, right)
    else:
        # If the length of the array is 1, then we have broken up the array enough so we just return the array
        return arr

    return merged_arr

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    # First, we determine a starting index for the "right" half of the array 
    start2 = mid + 1

    # Next, we write a while loop that will run until we have gone through one or both sides of the array
    while (start <= mid and start2 <= end):
        # The first thing we check in the while loop is whether the "left" and "right" elements we're looking at are already sorted (smaller on left, larger on right), and if they are, we increment the start index on the "left" array and go through the loop again
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            # If the "right" element is greater than the "left" element, we set variables to point at the value and index of the "right" element that we are looking at
            value, index = arr[start2], start2

            # Then we write a while loop that will stop when the current index is equivalent to the start index
            while (index is not start):
                # During each loop, we are setting the value at the current index to the value at the index to the left of it, slowly moving the value to the right 
                arr[index] = arr[index - 1]
                index -= 1
            
            # Once the element has been moved to the left enough, we 
            arr[start] = value

            # Finally, we increment each of the index variables so we can traverse through the array
            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    # First, we write an if statement to check if the left index is less than the right index, so the function will run until the array is broken down into single element arrays, as the left index will then equal the right index
    if (l < r):
        # If l < r, then we set a variable to the middle index
        middle = (l + r) // 2

        # Next, we recursively call merge_sort_in_place() on the "left" side of the array until l >= r, at which point we start backtracking through the stack to hit the "right" side of each array
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle + 1, r)

        # Once we have split an array into single element arrays, we call the helper function merge_in_place() and pass it
        merge_in_place(arr, l, middle, r)
        # print(arr)


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
