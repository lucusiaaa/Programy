import math


def getNumber():
    num = input("Insert the number: ")
    num = int(num)
    return num


def numberOfZerosAtTheEndOfFactorial(number):
    count = 0
    if number == 0:
        count = "can't calculate the zeros number from infinity"
    else:
        x = int(math.log(number, 5))
        for n in range(x):
            count = count + int(number * math.pow(0.2, n + 1))
    print("Number of zeros at the end of factorial is: " + str(count))

numberOfZerosAtTheEndOfFactorial(getNumber())