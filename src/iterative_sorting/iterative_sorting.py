# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i] and arr[j] < arr[smallest_index]:
                arr[cur_index], arr[j] = arr[j], arr[cur_index]
            j += 1

        # TO-DO: swap

    return arr


# print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arr_end = len(arr)-1
    # * Each iteration moves the largest accessible value to the end, so i=2 will move the second largest number to the second-to-last index. That means the end of the loop can decrement after each iteration.
    for i in range(0, arr_end):
        j = 0
        # * The inner loop, in turn, only needs to run while j is less than the latest 'ending' index. This keeps the loop from needing to check the entire array
        while j < arr_end:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        arr_end -= 1
        i += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
