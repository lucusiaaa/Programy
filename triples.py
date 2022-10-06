import random
def rand():
    randomlist = []
    for i in range(0,5):
        n = random.randint(1,30)
        randomlist.append(n)
    randomlist.sort()
    print(randomlist)
    return randomlist


def triples(sortedArr):
    arr = sortedArr.copy()
    out = []

    [[[[out.append([a, b, c]) if (c < a + b) else []] for inxc, c in enumerate(arr[inxb + 1:])] for inxb, b in
            enumerate(arr[inxa + 1:])] for inxa, a in enumerate(arr)]

    return out


# print(triples([1,2,3]))
print(triples([2, 3, 4, 5, 8]))
# print(triples(rand()))


