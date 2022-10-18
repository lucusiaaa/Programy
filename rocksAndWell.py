# Return an array.
# This function get string from user and change it into array,
# but he should separate.
# User should pass digits from the keyboard.
def getArrays():
    rocks = [i for i in input("Insert the diameters of rocks: ").split(",")]
    well = [j for j in input("Insert the diameters of well levels: ").split(",")]

    if rocks == ['']:
        rocks = []
    elif well == ['']:
        well = []
    else:
        rocks = list(map(int, rocks))
        well = list(map(int, well))

    return [rocks, well]


# This function takes array containing diameters of the well and rocks
# and calculate number of rocks which will fit into a well.
# Returns number of rocks.
def rockAndWell(arr):
    rocks, well = arr.copy()
    deep = len(well)
    count = 0
    newRocks = rocks[0:len(well)]

    newWell = []
    mini = well[0]
    for level in range(deep):
        mini = min(mini, well[level])
        newWell.append(mini)

    rock = 0
    if len(newWell) != 0 and len(newRocks) != 0:
        for i in range(1, deep + 1):
            if newRocks[rock] <= newWell[-i]:
                count += 1
                rock += 1
                if rock >= len(newRocks):
                    break
    elif len(newWell) == 0:
        print("There is no well here!")
    else:
        print("There are no rocks you can put into the well!")
    return count


print("Number of rocks in the well: ", rockAndWell(getArrays()))
