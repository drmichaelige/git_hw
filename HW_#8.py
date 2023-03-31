
# code here HW8_#1 Selection sort

def selection_sort(arr: list):
   for i in range(len(arr)):

    # Find the minimum element in remaining
    # unsorted array
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

    # Swap the found minimum element with
    # the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

test_list = [9, 8, 2, 1, 6, 4, 7]
print(test_list)
print(selection_sort(test_list))

# code here HW8_#2 Bubble sort


def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_list = [9, 8, 2, 1, 6, 4, 7]
print(test_list)
print(bubble_sort(test_list))

# code here HW8_#3 Insertion sort

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


test_list = [9, 8, 2, 1, 6, 4, 7]
print(test_list)
print(insertion_sort(test_list))


# code here HW8_#4 Merge sort

def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_arr: list, right_arr: list):
    merged_list = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_list.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_list.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] <= right_arr[j]:
            merged_list.append(left_arr[i])
            i += 1
        else:
            merged_list.append(right_arr[j])
            j += 1
    return merged_list


test_list = [9, 8, 2, 1, 6, 4, 7]
print(test_list)
print(merge_sort(test_list))