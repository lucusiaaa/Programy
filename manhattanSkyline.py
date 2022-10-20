# Returns integer.
# This function takes array of nonnegative integers which are the height equivalent of the Manhattan Skyline buildings
# and searches for the area of the biggest rectangle that could fit into shape created by Manhattan Skyline.
# Returns area of the biggest rectangle in this shape.
def manhattanSkyline(array):
    if not array:
        return

    amountOfLists = max(array)
    listOfMaxWidths = []
    count = 0
    for row in range(1, amountOfLists + 1):
        maxi = 0
        for column in array:
            if column >= row:
                count += 1
                if count > maxi:
                    maxi = count
            else:
                if count > maxi:
                    maxi = count
                    count = 0
                else:
                    count = 0
        count = 0
        listOfMaxWidths.append(maxi)

    maxArea = 0
    for i in range(amountOfLists):
        area = listOfMaxWidths[i] * (i + 1)
        if area > maxArea:
            maxArea = area
    return maxArea


def tests():
    assert (manhattanSkyline([3, 1, 4, 3, 5, 7, 5, 4, 1, 0, 3, 5, 0, 9, 8])) == 18
    assert (manhattanSkyline([0, 0, 0, 10, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1])) == 11
    assert (manhattanSkyline([])) is None


tests()
print("Area of the biggest rectangle in shape created by Manhattan Skyline: ", manhattanSkyline([3, 1, 4, 3, 5, 7, 5, 4, 1, 0, 3, 5, 0, 9, 8]))
