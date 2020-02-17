# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # print(f'outer loop -- smallest_index = {smallest_index}')
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            # print(f'inner loop | j = {j} || arr[j] = {arr[j]}')
            if arr[j] < arr[i] and arr[j] < arr[smallest_index]:
                # print(
                #     f'{arr[j]} is less than {arr[i]} and is also less than {arr[smallest_index]}')
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

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
