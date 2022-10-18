import random


def rand():
    randomlist = []
    for i in range(0, 10):
        n = random.randint(1, 30)
        randomlist.append(n)
    print(randomlist)
    return randomlist


# Returns tuple of two indexes.
# This function takes array of nonnegative integers and searches the biggest differences in subarrays
# consisting of integers from N to the end of array.
# Returns tuple of two indexes of numbers that create the biggest difference.
def stockProfit(array):
    results = []
    subArray = array.copy()

    for i in range(len(array)):
        maximum = max(subArray)
        lookingMinArray = subArray[0:subArray.index(maximum) + 1]
        minimum = min(lookingMinArray)
        # print(i, "| min: ", minimum, "| max: ", maximum)
        difference = maximum - minimum
        results.append([array.index(minimum, i), array.index(maximum, i), difference])
        subArray = subArray[1:]
    differences = []
    for i in results:
        differences.append(i[2])

    maxDiff = max(differences)
    indexOfMaxDiff = differences.index(maxDiff)
    # print("Wyniki: ", results)
    # print("Index: ", indexOfMaxDiff, " | Wybrany wynik: ", results[indexOfMaxDiff])
    return results[indexOfMaxDiff][0], results[indexOfMaxDiff][1]


def tests():
    assert(stockProfit([0])) == (0, 0)
    assert(stockProfit([7, 0])) == (0, 0)
    assert(stockProfit([2, 6, 2, 4, 1])) == (0, 1)


tests()
print(stockProfit([2, 6, 2, 4, 1]))
# print(stockProfit([7, 0]))
# print(stockProfit([0]))

# print(stockProfit(rand()))
