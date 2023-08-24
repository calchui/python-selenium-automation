#                           Level 1
# ************************** Problem 1 **************************

# def bingo(n: int):
#
#     for i in range(1, 101):
#
#         if i % 3 == 0 and i % 7 == 0:
#             print('BinGo')
#         elif i % 3 == 0:
#             print('Bin')
#         elif i % 7 == 0:
#             print('Go')
#         else:
#             print(i)
#
# bingo(101)

# ************************** Problem 2 **************************

# def sum_of_numbers(n: int):
#
#     total_sum = 0
#
#     for i in range(1, n + 1):
#
#         total_sum = total_sum + i
#
#     print(total_sum)
#
# sum_of_numbers(5)
# sum_of_numbers(8)

#                          Level 2
# ************************** Problem 1 **************************

# def find_max(a: int, b: int, c: int):
#
#     if a > b and a > c:
#         print(f'Max is {a}')
#     elif b > a and b > c:
#         print(f'Max is {b}')
#     elif c > a and c > a:
#         print(f'Max is {c}')
#
# find_max(10, 8, 6)
# find_max(8, 15, 6)
# find_max(6, 8, 20)

# ************************** Problem 2 **************************

# def leap_year(year: int):
#
#     if year % 4 == 0:
#
#         if year % 100 == 0 and year % 400 == 0:
#             print(f'{year} is a Leap Year')
#
#         elif year % 100 == 0 and year % 400 != 0:
#             print(f'{year} is not a Leap Year')
#
#     else:
#         print(f'{year} is not a Leap Year')
#
#
# leap_year(1998)
# leap_year(2000)
# leap_year(2100)


#                             Level 3
# ************************** Problem 1 **************************

def generate_fibonacci_sequence(n: int):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):


    # Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]
    n = n + (n - 1)
    # Append the new Fibonacci number to the list using the append() function
        fib_sequence.append(i)

    return fib_sequence

