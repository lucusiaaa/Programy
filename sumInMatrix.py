# Returns 2D array (n x m).
# This function receives array (n x m) and returns array (n x m), where element [i, j] is sum of all elements
# from position [0,0] to position [i,j].
def matrixOfsums(matrix):
    matrixOfSums = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                matrixOfSums[i][j] = matrix[i][j]
            else:
                if i == 0:
                    matrixOfSums[i][j] = matrixOfSums[i][j - 1] + matrix[i][j]
                elif j == 0:
                    matrixOfSums[i][j] = matrixOfSums[i - 1][j] + matrix[i][j]
                else:
                    matrixOfSums[i][j] = matrixOfSums[i][j - 1] + matrixOfSums[i - 1][j] + matrix[i][j] - \
                                         matrixOfSums[i - 1][j - 1]
    return matrixOfSums


# This function receives array and number.
# Returns subarray of passed array which sum of all elements equals to the number taken as parameter.
def summarizedRectangle(array, number):
    horizontal = len(array[0])
    vertical = len(array)
    matrix = matrixOfsums(array)
    sums = 0
    # s <- start point
    sx = 0
    sy = 0
    # e <- end point
    ex = 0
    ey = 0
    finMatrix = []

    while True:
        if horizontal >= vertical:
            while ey < len(matrix):
                while ex < len(matrix[0]):
                    sums = chosenSums(ex, ey, matrix, sx, sy)

                    if sums > number:
                        sx += 1
                        continue
                    if sums < number:
                        ex += 1
                    if sums == number:
                        for i in array[sy:ey + 1]:
                            finMatrix.append(i[sx:ex + 1])
                        return finMatrix
                ey += 1
                ex = 0
                sx = 0
            sy += 1
            ey = sy
            if sy == len(matrix) and ey == len(matrix):
                return []
        else:
            while ex < len(matrix[0]):
                while ey < len(matrix):
                    sums = chosenSums(ex, ey, matrix, sx, sy)

                    if sums > number:
                        sy += 1
                        continue
                    if sums < number:
                        ey += 1
                    if sums == number:
                        for i in array[sy:ey + 1]:
                            finMatrix.append(i[sx:ex + 1])
                        return finMatrix
                ex += 1
                ey = 0
                sy = 0
            sx += 1
            ex = sx
            if sx == len(matrix[0]) and ex == len(matrix[0]):
                return []


def chosenSums(ex, ey, matrix, sx, sy):
    if sy == 0 and sx == sy:
        sums = matrix[ey][ex]
    elif sy == 0:
        sums = matrix[ey][ex] - matrix[ey][sx - 1]
    elif sx == 0:
        sums = matrix[ey][ex] - matrix[sy - 1][ex]
    else:
        sums = matrix[ey][ex] - matrix[ey][sx - 1] - matrix[sy - 1][ex] + matrix[sy - 1][sx - 1]
    return sums


arr = [[3, 6, 0, 6, 5, 8, 4, 9],
       [1, 9, 8, 4, 6, 1, 2, 9],
       [1, 9, 8, 4, 6, 7, 2, 9],
       [1, 4, 8, 4, 6, 7, 2, 9],
       [1, 7, 3, 9, 5, 9, 9, 6],
       [2, 5, 9, 8, 0, 3, 8, 4],
       [1, 1, 6, 6, 7, 8, 0, 400]]

print(summarizedRectangle(arr, 10))
