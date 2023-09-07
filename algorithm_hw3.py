#          Task 1. Two Lowest Elements
def find_two_lowest(arr: list):

    result = arr[0]

    for num in arr:

        if num < result:

            result = num

    return result

numbers = [198, 3, 4, 9, 10, 9, 2]
print(f'Lowest number : {find_two_lowest(numbers)}')


#           Task 2
def invert_list(arr: list):
# Loop through each index of the array
    result = []

    for num in arr:

        num = num * -1

        result.append(num)

    return result

numbers = [1, 5, -2, 4]
print(f'Numbers: {numbers}')
print(f'Inverted numbers: {invert_list(numbers)}')

#           Task 3
def max_diff(arr: list):

    if len(arr) == 0:

        return 0

    print(sorted(arr))

    for i in range(len(arr)):

        #result = arr[3] - arr[0]

        result = max(arr) - min(arr)

    return result

numbers = (sorted([3, 5, 7, 2]))
print(f'The difference is {max_diff(numbers)}')


#           Task 4
def count_larger_neighbors(arr: list):

 # Initialize a variable 'count' to 0. This variable will keep track of the number of elements
# that are larger than both their adjacent neighbors.
    count = 0

# Loop through the list from index 1 to len(arr) - 2. We skip the first and the last elements
# because they don't have both left and right neighbors.
    for i in range(1, len(arr) - 1):

# Check if the current element (arr[i]) is greater than its left neighbor (arr[i - 1])
# and its right neighbor (arr[i + 1]).

        if i < arr[i - 1] and i > arr[i + 1]:

                print(i)

        return

print(count_larger_neighbors([2, 56, 7, 21, 22, 19, 26]))



#           Task 5
def subtract_min(arr: list):

    for num in arr:

        min_element = min(arr)

    return min_element

numbers = ([9, 2, 5, 4, 7, 6, 1])

print(numbers)

print(f'The minimum element in the list: {subtract_min(numbers)}')

numbers = ([9, 2, 5, 4, 7, 6, 1])
min_element = [1]

subtraction_result = []

for i in range(len(numbers)):

    result = numbers[i] - min_element[0]

    subtraction_result.append(result)

print(subtraction_result)


