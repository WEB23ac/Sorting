# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i] and arr[j] < arr[smallest_index]:
                smallest_index = j
                smallest_val = arr[smallest_index]
                swap_val = arr[cur_index]
                arr[cur_index] = smallest_val
                arr[smallest_index] = swap_val
            j += 1

        # TO-DO: swap

    return arr


# print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    arr_end = len(arr)-1
    for i in range(0, arr_end):
        j = 0
        while j < arr_end:
            if arr[j] > arr[j+1]:
                left_val = arr[j]
                right_val = arr[j+1]
                arr[j] = right_val
                arr[j+1] = left_val
            j += 1
        arr_end -= 1
        i += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
