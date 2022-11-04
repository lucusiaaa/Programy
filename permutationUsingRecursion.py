# Returns array.
# This function takes integer N as parameter and returns array consisting of numbers from 1 to N.
def arrayFromNumber(N):
    return list(range(1, N + 1))


# Returns array of arrays
# This function takes an array as a parameter and returns all possible permutations of this array elements.
def permutation(arr):
    # newArr <- single permutation
    newArr = []
    # allArr <- array with all permutations
    allArr = []

    if len(arr) >= 2:
        for i in range(len(arr)):
            for j in permutation(arr[:i]+arr[i+1:]):
                j.append(arr[i])
                newArr = j
                allArr.append(newArr)
        return allArr
    else:
        return [arr]


print(permutation(arrayFromNumber(3)))
