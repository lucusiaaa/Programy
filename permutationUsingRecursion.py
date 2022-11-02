# Returns array.
# This function takes integer N as parameter and returns array consisting of numbers from 1 to N.
def arrayFromNumber(N):
    return [i for i in range(1, int(N + 1))]


# Returns array
# This function takes integer and array as parameters and returns new array in which passed element doesn't appear.
def skipElementInArr(element, arr):
    newArr = []
    for i in arr:
        if i == element:
            continue
        else:
            newArr.append(i)
    return newArr


# Returns array of arrays
# This function takes an array as a parameter and returns all possible permutations of this array elements.
def permutation(arr):
    # newArr <- single permutation
    newArr = []
    # allArr <- array with all permutations
    allArr = []

    if len(arr) >= 2:
        for i in arr:
            for j in permutation(skipElementInArr(i, arr)):
                j.insert(0, i)
                newArr = j
                allArr.append(newArr)
        return allArr
    else:
        return [arr]


print(permutation(arrayFromNumber(3)))
