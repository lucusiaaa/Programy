# Return an array.
# This function get string from user and change it into array.
# User can pass any character from the keyboard.
def getArr():
    strin = input("Insert the string: ")
    arr = list(strin)
    return arr


# This function takes two arrays as parameters
# and interlocks their elements.
# Return an array.
def mixArrays(arr1, arr2):
    arr3 = [None] * (min(len(arr1), len(arr2))) * 2

    for i in range(min(len(arr1), len(arr2))):
        arr3[i * 2] = arr1[i]
        arr3[(i * 2) + 1] = arr2[i]

    if (len(arr1) > len(arr2)):
        arr4 = arr1[min(len(arr1), len(arr2)):]
    else:
        arr4 = arr2[min(len(arr1), len(arr2)):]

    arr3 += arr4
    return arr3


def tests():
    assert (mixArrays(['q', 'w', 'e', 'r', 't', 'y'], ['1', '2', '3']) == ['q', '1', 'w', '2', 'e', '3', 'r', 't', 'y'])
    assert (mixArrays(['1', '2', '3'], ['q', 'w', 'e', 'r', 't', 'y']) == ['1', 'q', '2', 'w', '3', 'e', 'r', 't', 'y'])


tests()
print(mixArrays(getArr(), getArr()))
