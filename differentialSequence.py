from numpy import *


# Return a list.
# This function get string from user and change it into list of integers.
# User can pass several numbers from the keyboard, separating them with a comma.
def getArr():
    arr = [int(i) for i in input("Enter the list items : ").split(",")]
    return arr

# TODO: zastanowic sie jaka role pelnia poszczegolne elementy i
#  robic to w kazdym kroku wszytkiego
# Return an array of arrays.
# This function take as parameter one array consists of numbers
# and calculate differential sequence b(n)=a(n-1)-a(n).
# Returns array consisting of all
# possible differential sequences of the imputed array.
def differentialSequence(arr):
    bigArr = []
    size = len(arr)

    # TODO: to jest jeden element, a poprawic tak zeby bylo ze jest pusta []
    # Jej wynikiem powinno byc [[]]
    # Wcześniej wykasowac, zeby eneter nie podawal tgo znaku
    if (arr == ['']):
        return bigArr

    # TODO: przed wejsciem bigarray nie zawiera arr
    #  trzeba pamietac ze na koncu zawsze dokleic ostani element

    # TODO: size ma byc >0, nie ma byc wgl notEmpty
    #  a poza whilem dokleic do bigarray array

    # TODO: niezmiennik pętli
    #  dodac go jako kontrakt (zagwarantowac to przed wejsciem do pętli i po kazdym kroku
    while (size > 0):
        bigArr.append(arr)

        # TODO: zamiast deklarowac supparr jako none, mozna doklejac do konca tablicy appendem
        suppArr = [None] * (size - 1)
        for i in range(size - 1):
            suppArr[i] = int(arr[i + 1]) - int(arr[i])

        arr = suppArr.copy()
        size = len(arr)

    bigArr.append(arr)
    return bigArr

# TODO: dodac test na pustej tablicy (powinien zwracac [[]])
#  Zmienic program tak, zeby zwracal podwojna tablice w tablicy
def tests():
    assert (differentialSequence([1, 2, 3, 4])) == [[1, 2, 3, 4], [1, 1, 1], [0, 0], [0], []]
    assert (differentialSequence([1, 10, 3, 0, 5])) == [[1, 10, 3, 0, 5], [9, -7, -3, 5], [-16, 4, 8], [20, 4], [-16], []]


tests()
print(differentialSequence(getArr()))
