# Returns integer.
# This function returns integer which is an amount of times the passed number appears in 2D array.
def numberInMatrix(matrix, number):
    if matrix == [[]] or matrix == []:
        return 0
    if matrix is None:
        return None

    # allNumbers <- storage an amount of times the passed number appears in matrix
    allNumbers = 0
    # x, y <- at the beginning: coordinates of the upper right element in matrix
    y = len(matrix[0]) - 1
    x = 0
    # checked <- element currently being checked
    checked = matrix[x][y]

    while True:
        if checked > number:
            y -= 1
        elif checked < number:
            x += 1
        else:
            allNumbers += 1
            x += 1
            y -= 1
            if x > len(matrix) - 1 or y < 0:
                return allNumbers
        if y < 0 or x > len(matrix) - 1:
            return allNumbers
        checked = matrix[x][y]


def tests():
    arr = [[]]
    assert numberInMatrix(arr, 11) == 0
    arr = [[1, 3, 7, 8, 10],
           [2, 5, 8, 9, 11],
           [5, 6, 9, 11, 13],
           [10, 11, 13, 15, 16],
           [11, 13, 14, 17, 20],
           [12, 14, 15, 20, 23]]
    assert numberInMatrix(arr, 11) == 4
    assert numberInMatrix(arr, 14) == 2
    assert numberInMatrix(arr, 15) == 2
    assert numberInMatrix(arr, 30) == 0


tests()

arr = [[1, 3, 7, 8, 10],
       [2, 5, 8, 9, 11],
       [5, 6, 9, 11, 13],
       [10, 11, 13, 15, 16],
       [11, 13, 14, 17, 20],
       [12, 14, 15, 20, 23]]

print(numberInMatrix(arr, 15))
