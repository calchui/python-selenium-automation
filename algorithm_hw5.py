
#           Descending Order Homework 5

def selection_sort(arr: list):
    for i in range(len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr

test_data = [2, 1, 0, 3, 4, 5]
print(test_data)
selection_sort(test_data)
print(test_data)


def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
test_data = [7, 6, 10, 9, 8]
print(test_data)
bubble_sort(test_data)
print(test_data)

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr

test_data = [15, 11, 14, 13, 12]
print(test_data)
insertion_sort(test_data)
print(test_data)