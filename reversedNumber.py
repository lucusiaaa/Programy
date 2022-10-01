# Return a number.
# This function get string from user and change it into integer.
def getNumber():
    num = int(input("Insert the number: "))
    return num


# This function takes one number as parameter
# and calculate reversed number.
# Return an integer.
def reverseNumber(number):
    size = len(str(number))
    reversedNumber = 0

    for i in range(size):
        lastDigit = number % 10
        reversedNumber = reversedNumber + lastDigit * 10**(size-(i+1))
        number = int(number / 10)

    return reversedNumber


def tests():
    assert (reverseNumber(1000) == 1)
    assert (reverseNumber(123) == 321)
    assert (reverseNumber(0) == 0)
    assert (reverseNumber(1) == 1)


changed = reverseNumber(getNumber())
tests()
print("Reversed number: ", changed)
