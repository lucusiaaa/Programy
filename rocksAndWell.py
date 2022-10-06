# Return an array.
# This function get string from user and change it into array,
# but he should separate .
# User should pass digits from the keyboard.
def getArrays():
    rocks = [int(i) for i in input("Insert the diameters of rocks: ").split(",")]
    well = [int(j) for j in input("Insert the diameters of well levels: ").split(",")]
    return [rocks, well]


def rockAndWell(arr):
    rocks, well = arr.copy()
    deep = len(well)
    count = 0

    newRocks = [rocks[i] for i in range(min(deep, len(rocks)))]

    newWell = []
    newWell.append(well[0])
    mini = max(well)
    for level in range(1, deep):
        mini = min(mini, well[level], well[level - 1])
        newWell.append(mini)

    for rock in newRocks:
        i = 0
        for level in newWell:
            if rock > level and i > 0:
                newWell = newWell[0:(i - 1)]
                count += 1
                break

            if rock > newWell[0]:
                return count

            if rock <= level and i <= deep - 1:
                count += 1
                break

            i += 1

    return count


print("Number of rocks in the well: ", rockAndWell(getArrays()))
