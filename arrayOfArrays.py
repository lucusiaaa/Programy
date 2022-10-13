# Return a list.
# This function get string from user and change it into array.
# User can pass any character from the keyboard.
def getArr():
    strIn = input("Insert the string: ")
    arr = list(strIn)
    return arr


# Return an array of arrays.
# This function take one array as parameter
# and returns array consisting of all
# possible sufixes of the imputed array.
def arrayOfSufixes(arr):
    suppArr = arr.copy()
    bigArr = []
    for i in range(len(suppArr) + 1):
        bigArr.append(suppArr[i:])
    return bigArr


def tests():
    assert (arrayOfSufixes(['q', 'w', 'e', 'r'])) == [['q', 'w', 'e', 'r'], ['w', 'e', 'r'], ['e', 'r'], ['r'], []]
    assert (arrayOfSufixes(['1', '!', ' ', 'q'])) == [['1', '!', ' ', 'q'], ['!', ' ', 'q'], [' ', 'q'], ['q'], []]


tests()
print(arrayOfSufixes(getArr()))
