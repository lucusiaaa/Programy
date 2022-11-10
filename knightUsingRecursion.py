import copy
import timeit


# Tworzy dziurawą szachownicę
def createChessboard():
    return [[True, None, True, True, None, True, True, True],
            [True, None, True, True, None, True, True, None],
            [None, True, None, True, True, True, True, None],
            [True, None, True, None, None, True, True, True],
            [True, None, True, None, True, True, None, True],
            [True, None, True, True, None, True, True, None],
            [None, True, None, None, True, True, None, None],
            [True, None, True, True, True, None, None, True]]


def createChessboard2():
    return [[True, None, True],
            [True, True, True],
            [None, True, True]]


# Wypisanie dziurawej szachownicy
def printChessboard(chessboard):
    for i in chessboard:
        for j in i:
            if j is None:
                print("- ", end="")
            elif j:
                print("O ", end="")
            else:
                print("X ", end="")
        print()


# Oblicza wszystkie ruchy, które może wykonać koń
def possibleMoves(x, y, chessboard):
    allPossibleMoves = []
    if 0 <= x + 2 <= 7 and 0 <= y - 1 <= 7 and chessboard[y - 1][x + 2] is True:
        allPossibleMoves.append([x + 2, y - 1])
    if 0 <= x + 2 <= 7 and 0 <= y + 1 <= 7 and chessboard[y + 1][x + 2] is True:
        allPossibleMoves.append([x + 2, y + 1])
    if 0 <= x - 2 <= 7 and 0 <= y - 1 <= 7 and chessboard[y - 1][x - 2] is True:
        allPossibleMoves.append([x - 2, y - 1])
    if 0 <= x - 2 <= 7 and 0 <= y + 1 <= 7 and chessboard[y + 1][x - 2] is True:
        allPossibleMoves.append([x - 2, y + 1])
    if 0 <= x + 1 <= 7 and 0 <= y - 2 <= 7 and chessboard[y - 2][x + 1] is True:
        allPossibleMoves.append([x + 1, y - 2])
    if 0 <= x + 1 <= 7 and 0 <= y + 2 <= 7 and chessboard[y + 2][x + 1] is True:
        allPossibleMoves.append([x + 1, y + 2])
    if 0 <= x - 1 <= 7 and 0 <= y - 2 <= 7 and chessboard[y - 2][x - 1] is True:
        allPossibleMoves.append([x - 1, y - 2])
    if 0 <= x - 1 <= 7 and 0 <= y + 2 <= 7 and chessboard[y + 2][x - 1] is True:
        allPossibleMoves.append([x - 1, y + 2])
    return allPossibleMoves


# def possibleMoves(x, y, chessboard):
#     allPossibleMoves = []
#     if 0 <= x + 2 <= 2 and 0 <= y - 1 <= 2 and chessboard[y - 1][x + 2] is True:
#         allPossibleMoves.append([x + 2, y - 1])
#     if 0 <= x + 2 <= 2 and 0 <= y + 1 <= 2 and chessboard[y + 1][x + 2] is True:
#         allPossibleMoves.append([x + 2, y + 1])
#     if 0 <= x - 2 <= 2 and 0 <= y - 1 <= 2 and chessboard[y - 1][x - 2] is True:
#         allPossibleMoves.append([x - 2, y - 1])
#     if 0 <= x - 2 <= 2 and 0 <= y + 1 <= 2 and chessboard[y + 1][x - 2] is True:
#         allPossibleMoves.append([x - 2, y + 1])
#     if 0 <= x + 1 <= 2 and 0 <= y - 2 <= 2 and chessboard[y - 2][x + 1] is True:
#         allPossibleMoves.append([x + 1, y - 2])
#     if 0 <= x + 1 <= 2 and 0 <= y + 2 <= 2 and chessboard[y + 2][x + 1] is True:
#         allPossibleMoves.append([x + 1, y + 2])
#     if 0 <= x - 1 <= 2 and 0 <= y - 2 <= 2 and chessboard[y - 2][x - 1] is True:
#         allPossibleMoves.append([x - 1, y - 2])
#     if 0 <= x - 1 <= 2 and 0 <= y + 2 <= 2 and chessboard[y + 2][x - 1] is True:
#         allPossibleMoves.append([x - 1, y + 2])
#     return allPossibleMoves


# Aktualizuje pole, które odwiedził koń
def updateChessboardField(x, y, chessboard):
    if chessboard[y][x] is True:
        chessboard[y][x] = False
    return chessboard


def move(x=0, y=0, chessboard=createChessboard()):
    # updatedChessboard <- nowa plansza ze zaktualizowanym polem na którym stoimy
    updatedChessboard = copy.deepcopy(chessboard)
    updatedChessboard = updateChessboardField(x, y, updatedChessboard)
    if len(possibleMoves(x, y, updatedChessboard)) > 1:
        maxCount = 0
        maxChessBoard = []
        for oneX, oneY in possibleMoves(x, y, updatedChessboard):
            moveCount, board = move(oneX, oneY, copy.deepcopy(updatedChessboard))
            if moveCount > maxCount:
                maxCount = copy.deepcopy(moveCount)
                maxChessBoard = copy.deepcopy(board)
        return [maxCount + 1, maxChessBoard]
    elif possibleMoves(x, y, updatedChessboard):
        x1, y1 = possibleMoves(x, y, updatedChessboard)[0]
        moveCount, board = copy.deepcopy(move(x1, y1, updatedChessboard))
        return [moveCount + 1, board]
    else:
        return [0, updatedChessboard]


a, b = move()
print(a, b)
printChessboard(b)


def timer():
    print('functionName: ', timeit.timeit(move, number=1))


timer()
