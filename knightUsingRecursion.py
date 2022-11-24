import copy
import timeit


# Tworzy dziurawą szachownicę
def createChessboard():
    return [[0, -1, 0, 0, -1, 0, 0, 0],
            [0, -1, 0, 0, -1, 0, 0, -1],
            [-1, 0, -1, 0, 0, 0, 0, -1],
            [0, -1, 0, -1, -1, 0, 0, 0],
            [0, -1, 0, -1, 0, 0, -1, 0],
            [0, -1, 0, 0, -1, 0, 0, -1],
            [-1, 0, -1, -1, 0, 0, -1, -1],
            [0, -1, 0, 0, 0, -1, -1, 0]]


def createChessboard2():
    return [[0, -1, 0],
            [0, 0, 0],
            [-1, 0, 0]]


def createChessboard3():
    return [[0, -1, 0, 0, -1],
            [0, -1, 0, 0, -1],
            [-1, 0, -1, 0, 0],
            [0, -1, 0, -1, -1],
            [0, -1, 0, -1, 0]]

def createChessboard4():
    return [[0, -1, 0, 0, -1, 0, 0],
            [0, -1, 0, 0, -1, 0, 0],
            [-1, 0, -1, 0, 0, 0, 0],
            [0, -1, 0, -1, -1, 0, 0],
            [0, -1, 0, -1, 0, 0, -1],
            [0, -1, 0, 0, -1, 0, 0],
            [-1, 0, -1, -1, 0, 0, -1]]

# # Wypisanie dziurawej szachownicy
def printChessboard(chessboard):
    for i in chessboard:
        print(i)


# Oblicza wszystkie ruchy, które może wykonać koń
def possibleMoves(x, y, chessboard):
    allPossibleMoves = []
    length = len(chessboard) - 1
    if 0 <= x + 2 <= length and 0 <= y - 1 <= length and chessboard[y - 1][x + 2] == 0:
        allPossibleMoves.append([x + 2, y - 1])
    if 0 <= x + 2 <= length and 0 <= y + 1 <= length and chessboard[y + 1][x + 2] == 0:
        allPossibleMoves.append([x + 2, y + 1])
    if 0 <= x - 2 <= length and 0 <= y - 1 <= length and chessboard[y - 1][x - 2] == 0:
        allPossibleMoves.append([x - 2, y - 1])
    if 0 <= x - 2 <= length and 0 <= y + 1 <= length and chessboard[y + 1][x - 2] == 0:
        allPossibleMoves.append([x - 2, y + 1])
    if 0 <= x + 1 <= length and 0 <= y - 2 <= length and chessboard[y - 2][x + 1] == 0:
        allPossibleMoves.append([x + 1, y - 2])
    if 0 <= x + 1 <= length and 0 <= y + 2 <= length and chessboard[y + 2][x + 1] == 0:
        allPossibleMoves.append([x + 1, y + 2])
    if 0 <= x - 1 <= length and 0 <= y - 2 <= length and chessboard[y - 2][x - 1] == 0:
        allPossibleMoves.append([x - 1, y - 2])
    if 0 <= x - 1 <= length and 0 <= y + 2 <= length and chessboard[y + 2][x - 1] == 0:
        allPossibleMoves.append([x - 1, y + 2])
    return allPossibleMoves


def move(x=0, y=0, chessboard=createChessboard(), moveNr=0):
    chessboard[y][x] = moveNr + 1
    maxChessBoard = chessboard
    result = possibleMoves(x, y, chessboard)
    while result:
        oneMove = result.pop()
        tempChess = move(oneMove[0], oneMove[1], copy.deepcopy(chessboard), moveNr + 1)
        if max(max(tempChess)) >= max(max(maxChessBoard)):
            maxChessBoard = tempChess
    return copy.deepcopy(maxChessBoard)


chess = move()
printChessboard(chess)

# def timer():
#     print('functionName: ', timeit.timeit(move, number=1))
#
#
# timer()
