

test_array = [4, 233, 6, 1, 8, 3, 4]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # * [0,0,0,0,0,0]
    # TODO - performs actual sorting of elements in arrA and arrB
    for i in range(0, elements):
        if len(arrA) == 0:
            merged_arr[i:i+len(arrB)] = arrB
            arrB = []
        if len(arrB) == 0:
            merged_arr[i:i+len(arrA)] = arrA
            arrA = []

        else:
            if arrA[0] <= arrB[0]:
                merged_arr[i] = arrA[0]
                arrA = arrA[1:]
            elif arrA[0] >= arrB[0]:
                merged_arr[i] = arrB[0]
                arrB = arrB[1:]
            print(merged_arr)
    return merged_arr


def merge_sort(arr):
    # TO-DO
    # * holds value of array length
    arr_length = len(arr)
    # * Base Case
    # * if array length is one, it is already sorted, run recursive function if length is greater than 1

    # * if the length of the array is greater than one (ie until the array has a single element)
    # * divide sub arrays until their length is 1
    if arr_length > 1:
        # * make one array representing values on the left side of the array's partition containing entries beggining through array_length // 2
        partition = len(arr) // 2
        left_array = merge_sort(arr[0:partition])
        # * make a second array representing values on the right side of the array's partition -- containing entries (array_length // 2) + 1 through end
        right_array = merge_sort(arr[partition:])
        print(f'RIGHT_ARRAY : {right_array}')
        arr = merge(left_array, right_array)

    return arr


print(merge_sort([1]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
