"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.
"""


# Variant 1
# def square_digits(num):
#     string = ''
#     for digit in str(num):
#         string += str(int(digit)**2)
#     return int(string)

# Variant 2
# def get_digits(num):
#     if num == 0: return [0]
#     digits = []
#     res, rem = divmod(num, 10)
#     while res + rem != 0:
#         digits.append(rem)
#         res, rem = divmod(res, 10)
#     return digits[::-1]

# def square_digits(num):
#     return int("".join(map(str, map(lambda x: x**2, get_digits(num)))))

# Variant 3
def square_digits(num):
    return int("".join(map(str, map(lambda x: x ** 2, [int(digit) for digit in str(num)]))))


# Best practice
def square_digits(num):
    return int(''.join(str(int(c) ** 2) for c in str(num)))
