"""
DESCRIPTION:
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""


def row_sum_odd_numbers(n):
    numbers_before = sum(range(1, n))
    first_in_the_row = numbers_before * 2 + 1
    row = range(first_in_the_row, first_in_the_row + 2 * n, 2)
    return sum(row)


if __name__ == '__main__':
    print(row_sum_odd_numbers(1))
    print(row_sum_odd_numbers(2))