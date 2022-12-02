# Returns array and integer.
# This function checks if passed array contains subarray which summarized element are equal to passed integer.
def caterpillar(array, number):
    # start <- index indicating begin of the subarray
    start = 0
    # end <- index indicating end of the subarray
    end = 0
    # sum <- summarized elements in subarray
    suma = 0

    while end <= len(array) and start < len(array):
        if suma < number:
            if end < len(array):
                suma += array[end]
            end += 1
        elif suma > number:
            suma -= array[start]
            start += 1
        else:
            return array[start: end], number
    return None, number


# This function prints result of caterpillar() function
def printCaterpillar(caterpi, number):
    if caterpi is None:
        print("There is no sum which is equals to ", number)
    else:
        print(caterpi, "-> sum =", sum(caterpi))


def tests():
    result, number = caterpillar([1, 3, 10, 6, 3, 5, 2], 21)
    assert result is None
    result, number = caterpillar([1, 3, 10, 6, 3, 5, 2], 7)
    assert result == [5, 2]
    result, number = caterpillar([1, 3, 10, 8, 3, 5, 2], 21)
    assert result == [3, 10, 8]
    result, number = caterpillar([0, 0, 0, 1, 0, 0, 1, 0, 0], 2)
    assert result == [0, 0, 0, 1, 0, 0, 1]
    result, number = caterpillar([], 2)
    assert result is None


tests()

arr, num = caterpillar([1, 3, 10, 6, 3, 5, 2], 21)
printCaterpillar(arr, num)
arr, num = caterpillar([1, 3, 10, 8, 3, 5, 2], 21)
printCaterpillar(arr, num)
arr, num = caterpillar([0, 0, 0, 1, 0, 0, 1, 0, 0], 2)
printCaterpillar(arr, num)
arr, num = caterpillar([], 2)
printCaterpillar(arr, num)
arr, num = caterpillar([1, 3, 10, 6, 3, 5, 2], 7)
printCaterpillar(arr, num)
