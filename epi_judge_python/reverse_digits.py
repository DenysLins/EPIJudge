from test_framework import generic_test


def reverse(x: int) -> int:
    # TODO - you fill in here.
    result, remaining = 0, abs(x)
    print(result, remaining)
    while remaining:
        print(result * 10)
        print(remaining % 10)
        result = result * 10 + remaining % 10
        print result
        remaining = remaining // 10
    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
