import random


# TODO:
#  3 1 9 3 8 2 7 0 -> idziemy 0, max=0, maxProfit=0
#  3 1 9 3 8 2 7 0 -> idziemy 7, max=7, maxProfit=0 (bo sprzedajemy w przód a nie w tył)
#  3 1 9 3 8 2 7 0 -> idziemy 2, max=7, maxProfit=5 (bo 7 - 2 = 5)
#  3 1 9 3 8 2 7 0 -> idziemy 8, max=8, maxProfit=5
#  3 1 9 3 8 2 7 0 -> idziemy 3, max=8, maxProfit=5 (bo 8 - 3 = 5)
#  3 1 9 3 8 2 7 0 -> idziemy 9, max=9, maxProfit=5
#  3 1 9 3 8 2 7 0 -> idziemy 1, max=9, maxProfit=8 (bo 9 - 1 = 8)
#  3 1 9 3 8 2 7 0 -> idziemy 3, max=9, maxProfit=8 (8 > (9-3)=6)

# Returns tuple of two indexes.
# This function takes array of non-negative integers and searches the biggest differences between two numbers.
# The index of lower number has to appear before the index of bigger number.
# If maxProfit == 0, indexes of those numbers will be equals.
# Returns tuple of two indexes of numbers that create the biggest difference.
def stockProfit(array):
    if not array:
        return None

    maxi = 0
    maxProfit = 0
    indexMin = len(array) - 1
    indexMax = len(array) - 1

    for i in range(1, len(array) + 1):
        if array[-i] >= maxi:
            maxi = array[-i]
            test = len(array) - i
        elif maxProfit < maxi - array[-i]:
            maxProfit = maxi - array[-i]
            indexMax = test
            indexMin = len(array) - i

    return indexMin, indexMax


def tests():
    assert (stockProfit([])) is None
    assert (stockProfit([0, 0])) == (1, 1)
    assert (stockProfit([7, 0])) == (1, 1)
    assert (stockProfit([2, 6, 2, 4, 1])) == (0, 1)


tests()

print(stockProfit([1, 4, 8, 12, 0, 15]))
# print(stockProfit(rand()))
