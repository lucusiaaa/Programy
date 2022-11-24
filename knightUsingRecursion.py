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

    # TODO: tu po prostu przypisac do szachownicy [x,y] -> False
    # if len(possibleMoves(x, y, updatedChessboard)) > 1:
    #     maxCount = 0
    #     maxChessBoard = []
    #     for oneX, oneY in possibleMoves(x, y, updatedChessboard):
    #         # TODO: zamiast tego deepcopy
    #         moveCount, board = move(oneX, oneY, copy.deepcopy(updatedChessboard))
    #         if moveCount > maxCount:
    #             maxCount = moveCount
    #             maxChessBoard = board
    #     # TODO: tu przypisac szachownice [x,y] z powrotem na -> True
    #     return [maxCount + 1, maxChessBoard]
    # # TODO: ten człon wyrzucić i zawrzeć go w tym wyzej
    # elif possibleMoves(x, y, updatedChessboard):
    #     x1, y1 = possibleMoves(x, y, updatedChessboard)[0]
    #     moveCount, board = copy.deepcopy(move(x1, y1, updatedChessboard))
    #     return [moveCount + 1, board]
    # else:
    #     # TODO: tutaj dac deepcopy
    #     return [0, updatedChessboard]

#
# chess = move()
# # print(move())
# printChessboard(chess)

def timer():
    print('functionName: ', timeit.timeit(move, number=1))


timer()
