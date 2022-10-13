# This function takes sorted array of integers and
# returns array of triples containing integers that can create triangle.
def triples(sortedArr):
    arrA = sortedArr.copy()
    out = []
    ia = 0
    for a in arrA:
        if ia + 1 <= len(arrA):
            arrB = arrA[ia + 1:]
            ia += 1
            ib = 0
            for b in arrB:
                if ib + 1 <= len(arrB):
                    arrC = arrB[ib + 1:]
                    ib += 1
                    for c in arrC:
                        if c < a + b:
                            out.append([a, b, c])
    return out


def tests():
    assert (triples([]) == [])
    assert (triples([1,2,3]) == [])
    assert (triples([2, 3, 4, 5, 8]) == [[2, 3, 4], [2, 4, 5], [3, 4, 5], [4, 5, 8]])


# def flatten(list):
#     return [item for sublist in list for item in sublist]


# print(triples([1,2,3]))
# print(triples(rand()))
tests()
print(triples([2, 3, 4, 5, 8]))