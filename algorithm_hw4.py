#           Problem 1

def sum_even_and_product_odd(arr: list):
    # Initialize variables for the sum of even numbers and the product of odd numbers
    sum_even = 0
    product_odd = 1

    for i in arr:
        if i % 2 == 0:
            sum_even = sum_even + i

        else:
            product_odd = product_odd * i

    return sum_even, product_odd

print(sum_even_and_product_odd([1, 2, 3, 4]))


#           Problem 2

def sum_between_range(arr: list):
    min_index = 0
    max_index = 0

    for i in range(len(arr)):

        if arr[i] > arr[max_index]:

            max_index = i

        if arr[i] < arr[min_index]:

            min_index = i

    print([min_index, max_index])

    return sum(arr[min(min_index, max_index) + 1: max(min_index, max_index)])


print(sum_between_range([3, 1, 2, 4, 6, 8, 7, 10, 9, 5]))


#           Problem 3

def buy_and_sell_stock(prices: list):

    maximum_profit = 0

    for i in range(len(prices) - 1):

        if prices[i + 1] - prices[i] > 0:

            maximum_profit = maximum_profit + prices[i + 1] - prices[i]

    return maximum_profit


print(buy_and_sell_stock([7, 1, 5, 3, 6, 4]))


#           Problem 4

def plus_one(arr: list):


