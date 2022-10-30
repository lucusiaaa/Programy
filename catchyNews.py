# Returns array.
# This function takes array of non-negative integers which are equivalent to the incidence of COVID-19
# in the last X days and returns an array containing information on how long backwards this has been the case.
def catchyNews(array):
    if array:
        return None
    myArray = array.copy()
    stack = []
    limitIndexArray = []
    theGreatestFromArray = []

    for i in range(len(myArray)):
        if not stack:
            limitIndexArray.append(0)
        else:
            while stack != [] and myArray[i] > myArray[stack[-1]]:
                stack.pop()
            if not stack:
                limitIndexArray.append(0)
            else:
                limitIndexArray.append(stack[-1] + 1)
        stack.append(i)

    for i in range(len(limitIndexArray)):
        theGreatestFromArray.append(i - limitIndexArray[i] + 1)
    return theGreatestFromArray


def tests():
    assert (catchyNews([5, 7, 2, 4, 8, 3, 12, 1, 4, 2, 4, 6])) == [1, 2, 1, 2, 5, 1, 7, 1, 2, 1, 2, 5]
    assert (catchyNews([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert (catchyNews([4, 3, 2, 1])) == [1, 1, 1, 1]


tests()
print(catchyNews([5, 7, 2, 4, 8, 3, 12, 1, 4, 2, 4, 6]))
print(catchyNews([6, 5, 4, 2, 1]))
