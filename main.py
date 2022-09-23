import math


def getNumber():
    num = input("Podaj liczbę: ")
    print("Podano liczbę: " + num)
    return num


def getString(number):
    arr = []
    sizeOfNumber = len(number)
    for i in range(sizeOfNumber):
        arr.append(number[i])
    return arr


def changeString(number, arr):
    newArr = [None] * len(number)
    i = len(number) - 1
    j = 0
    finalNum = 0
    while i >= 0:
        newArr[i] = arr[j]
        i -= 1
        j += 1
    x = len(number)
    for i in range(x):
        finalNum = finalNum + int(newArr[i]) * math.pow(10, x - 1)
        x -= 1
    print(int(finalNum))
    return finalNum


num = getNumber()
changeString(num, getString(num))
