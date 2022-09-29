# Return an array.
# This function get string from user and change it into array.
# User can pass any character from the keyboard.
def getArr():
    strIn = input("Insert the string: ")
    arr = list(strIn)
    return arr

# Return an array of arrays.
# This function take one array as parameter
# and returns array consisting of all
# possible sufixes of the imputed array.
def arrayOfSufixes(arr):
    bigArr = []
    i = 0
    notEmpty = True

    suppArr = arr.copy()
    bigArr.append(suppArr)
    size = len(arr)

    while (notEmpty):
        arr.pop(0)
        bigArr.append(arr[i - (size):])
        i += 1
        if (arr == []):
            notEmpty = False

    return bigArr

    # TO DZIAŁA, ALE NIE ZWRACA PUSTEGO ELEMENTU
    # bigArr=[]
    # for i in range(len(arr)):
    #     bigArr.append(arr[-(len(arr)-i):])
    # return bigArr

print(arrayOfSufixes(getArr()))
