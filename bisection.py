# import timeit

# Returns an integer.
# This function take as parameter one sorted array which indexes are shifted by unknown amount.
# Returns the starting index of array before shifting.
def bisection(sortedArray):
    if not sortedArray:
        return None
    leftEnd = 0
    rightEnd = len(sortedArray) - 1
    while leftEnd < rightEnd:
        middle = leftEnd + int((rightEnd - leftEnd) / 2)
        if sortedArray[middle] > sortedArray[rightEnd]:
            leftEnd = middle + 1
        else:
            rightEnd = middle
    return middle


def tests():
    assert (bisection([1, 2, 3, 4, 5])) == 0
    assert (bisection([2, 3, 4, 5, 1])) == 4
    assert (bisection([1, 2, 3, 4, 5, 6])) == 0
    assert (bisection([2, 3, 4, 5, 6, 1])) == 5
    assert (bisection([4, 5, 1, 2, 3])) == 2
    assert (bisection([])) is None


# tests()
print("The index of the smallest element in the array: ", bisection([2, 3, 4, 1]))

# print("bisection runtime: ", timeit.timeit(bisection, number=1))
