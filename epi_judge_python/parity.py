from test_framework import generic_test

# V1
# def parity(x: int) -> int:
#     # TODO - you fill in here.
#     result = 0
#     while x:
#         result ^= x & 1
#         x >>= 1
#     return result


def parity(x: int) -> int:
    # V2
    # TODO - you fill in here.
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
