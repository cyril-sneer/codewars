"""
DESCRIPTION:
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
However, the arrays can have varying lengths, not just limited to 4.
"""


def binary_array_to_number(arr):
    number_in_dec = 0
    for index, value in enumerate(arr[::-1]):
        number_in_dec += value * 2 ** index
    return number_in_dec

# def binary_array_to_number(arr):
#     return int("".join(map(str, arr)), 2)


# def binary_array_to_number(arr):
#     return sum(2**i for i, n in enumerate(arr[::-1]) if n)


if __name__ == '__main__':
    print(binary_array_to_number([1, 1, 1, 1]))
    int(3)
