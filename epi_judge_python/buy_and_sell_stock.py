from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    maximum_profit = 0.0
    minimum_element = float('inf')
    for m in prices:
        if m < minimum_element:
            minimum_element = m
        if (m - minimum_element) > maximum_profit:
            maximum_profit = m - minimum_element
    return maximum_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
