import math
from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x <= 0:
        return x == 0

    n = math.floor(math.log10(x)) + 1
    msd_mask = math.pow(10, n - 1)

    for i in range(n // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
