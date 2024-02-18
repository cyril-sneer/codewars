"""
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Examples:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""


def high_and_low(numbers):
    numbers_lst_int = [int(num_str) for num_str in numbers.split()]
    # return " ".join(map(str, [max(numbers_lst_int), min(numbers_lst_int)]))
    return f"{max(numbers_lst_int)} {min(numbers_lst_int)}"


if __name__ == '__main__':
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))