# Returns integer.
# This function takes array of non-negative integers which are the height equivalent of the Manhattan Skyline buildings
# and searches for the area of the biggest rectangle that could fit into shape created by Manhattan Skyline.
# Returns area of the biggest rectangle in this shape.
def manhattanSkyline(array):
    if array == []:
        return None

    myArray = array.copy()
    myArray.append(0)
    stack = []
    maxArea = -2

    for i in range(len(myArray)):
        if stack == []:
            stack.append(i)
        elif myArray[i] >= myArray[stack[-1]]:
            stack.append(i)
        else:
            while stack != [] and myArray[i] < myArray[stack[-1]]:
                top = stack.pop()
                if stack == []:
                    area = myArray[top] * i
                else:
                    area = myArray[top] * (i - stack[-1] - 1)
                maxArea = max(maxArea, area)
            stack.append(i)
    return maxArea


# print("Area of the biggest rectangle in shape created by Manhattan Skyline: ",
#       manhattanSkyline([2,3,2,2,2]))

def tests():
    assert (manhattanSkyline([3, 1, 4, 3, 5, 7, 5, 4, 1, 0, 3, 5, 0, 9, 8])) == 18
    assert (manhattanSkyline([0, 0, 0, 10, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1])) == 11
    assert (manhattanSkyline([])) is None


tests()
print("Area of the biggest rectangle in shape created by Manhattan Skyline: ",
      manhattanSkyline([3, 1, 4, 3, 5, 7, 5, 4, 1, 0, 3, 5, 0, 9, 8]))