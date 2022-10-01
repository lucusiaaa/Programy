import math


# Return an integer.
# This function get string from user and change it into integer.
def getNumber():
    str = input("Insert the number: ")
    num = int(str)
    return num


# This function takes one number as parameter
# and calculate number of zeros at the end of factorial of this number.
# Return an integer.
def numberOfZerosAtTheEndOfFactorial(number):
    count = 0
    n = 0
    x = int(number / math.pow(5, n + 1))
    while x >= 1:
        count = count + x
        n += 1
        x = int(number / math.pow(5, n + 1))
    return count


def tests():
    assert (numberOfZerosAtTheEndOfFactorial(0) == 0)
    assert (numberOfZerosAtTheEndOfFactorial(12) == 2)
    assert (numberOfZerosAtTheEndOfFactorial(29) == 6)
    assert (numberOfZerosAtTheEndOfFactorial(126) == 31)


num = numberOfZerosAtTheEndOfFactorial(getNumber())
tests()
print("Number of zeros at the end of factorial is: ", num)
