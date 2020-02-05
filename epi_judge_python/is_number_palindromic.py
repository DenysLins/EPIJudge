import math
from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x < 0:
        return False

    if x == 0:
        return True

    n = float('inf')
    while n > 2 and x != 0:
        print('')
        print(x, x % 10)
        lsd = x % 10
        print('lsd', lsd)
        n = math.floor(math.log10(x)) + 1
        print('n', n)
        msd = int(x // math.pow(10, n-1))
        print('msd', msd)
        if (lsd != msd):
            return False
        else:
            x = int(x % (msd * math.pow(10, n-1)))
            x = x // 10
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
