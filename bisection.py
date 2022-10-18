# import timeit
# Returns an integer.
# This function take as parameter one sorted array which indexes are shifted by unknown amount.
# Returns the starting index of array before shifting.
def bisection(sortedArray):
    leftEnd = 0
    rightEnd = len(sortedArray) - 1
    middle = int(len(sortedArray) / 2)

    while sortedArray:
        if sortedArray[middle] < sortedArray[middle - 1]:
            return middle
        if middle == leftEnd:
            if sortedArray[middle] < sortedArray[rightEnd]:
                return middle
            else:
                return rightEnd
        if middle == rightEnd:
            if sortedArray[middle] < sortedArray[leftEnd]:
                return middle
            else:
                return leftEnd
        if sortedArray[middle] < sortedArray[leftEnd] and sortedArray[middle] < sortedArray[rightEnd]:
            rightEnd = middle - 1
        if sortedArray[middle] > sortedArray[leftEnd] and sortedArray[middle] > sortedArray[rightEnd]:
            leftEnd = middle + 1
        if sortedArray[middle] > sortedArray[leftEnd] and sortedArray[middle] < sortedArray[rightEnd]:
            rightEnd = middle - 1
        middle = leftEnd + int((rightEnd - leftEnd) / 2)


def cheated(sortedArray):
    minimum = min(sortedArray)
    indexMin = sortedArray.index(minimum)
    return indexMin


def tests():
    assert(bisection([1, 2, 3, 4, 5])) == 0
    assert(bisection([2, 3, 4, 5, 1])) == 4
    assert(bisection([1, 2, 3, 4, 5, 6])) == 0
    assert(bisection([2, 3, 4, 5, 6, 1])) == 5
    assert(bisection([4, 5, 1, 2, 3])) == 2
    assert(bisection([])) == None


tests()
print("The index of the smallest element in the array: ", bisection([4, 5, 1, 2, 3]))
# print("The index of the smallest element in the array: ", cheated([4, 5, 1, 2, 3]))
