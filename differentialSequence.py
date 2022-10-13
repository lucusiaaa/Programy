from numpy import *


# Return a list.
# This function get string from user and change it into list of integers.
# User can pass several numbers from the keyboard, separating them with a comma.
def getArr():
    arr = [i for i in input("Enter the list items : ").split(",")]
    if arr == ['']:
        return []
    else:
        arr = list(map(int, arr))
        return arr


# Return an array of arrays.
# This function take as parameter one array consists of numbers
# and calculate differential sequence b(n)=a(n-1)-a(n).
# Returns array consisting of all
# possible differential sequences of the imputed array.
def differentialSequence(arr):
    bigArr = []
    size = len(arr)

    while (size > 0):
        bigArr.append(arr)

        suppArr = []
        for i in range(size - 1):
            suppArr.append(int(arr[i + 1]) - int(arr[i]))

        arr = suppArr.copy()
        size = len(arr)

    bigArr.append(arr)
    return bigArr


def tests():
    assert (differentialSequence([])) == [[]]
    assert (differentialSequence([1, 2, 3, 4])) == [[1, 2, 3, 4], [1, 1, 1], [0, 0], [0], []]
    assert (differentialSequence([1, 10, 3, 0, 5])) == [[1, 10, 3, 0, 5], [9, -7, -3, 5], [-16, 4, 8], [20, 4], [-16],
                                                        []]


tests()
print(differentialSequence(getArr()))
