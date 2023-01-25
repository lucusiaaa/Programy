import heapq

'''
This function creates dictionary containing all vertices and the corresponding lists of
vertices to which they are connected by an edge.

:param matrix: matrix, which is a representation of the terrain map.
               Each value of the matrix corresponds to the elevation of the terrain at a given point on the map.
:return: dictionary which contains the vertices and the corresponding lists of vertices to which they
         are connected by an edge
'''
def addEdge(matrix):
    dictionaryWithEdges = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            listOfNeigh = []
            # Adding top neighbour
            if i != 0:
                listOfNeigh.append((i - 1, j))
            # Adding bottom neighbour
            if i != len(matrix) - 1:
                listOfNeigh.append((i + 1, j))
            # Adding left neighbour
            if j != 0:
                listOfNeigh.append((i, j - 1))
            # Adding right neighbour
            if j != len(matrix[i]) - 1:
                listOfNeigh.append((i, j + 1))

            dictionaryWithEdges[(i, j)] = listOfNeigh
    return dictionaryWithEdges


'''
This function creates dictionary containing all vertices with corresponding values.

:param matrix: matrix, which is a representation of the terrain map. 
               Each value of the matrix corresponds to the elevation of the terrain at a given point on the map.
:return: dictionary which contains the vertices and their corresponding values in the matrix
'''
def addVertex(matrix):
    dictionaryWithVertexes = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            dictionaryWithVertexes[(i, j)] = matrix[i][j]

    return dictionaryWithVertexes


'''
This function creates dictionary containing all vertices and info if a vertex 
has already been visited during a graph search.

:param matrix: matrix, which is a representation of the terrain map. 
               Each value of the matrix corresponds to the elevation of the terrain at a given point on the map.
:return dictionaryWithIsVisited: dictionary containing all vertices and info if vertex has already been visited 
                                 during a graph search.
'''
def addIsVisitedInfo(matrix):
    dictionaryWithIsVisited = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dictionaryWithIsVisited[(i, j)] = False
    return dictionaryWithIsVisited

'''
This function takes a matrix of size nxm and finds the path that has the lowest height 
(not necessarily the shortest and not necessarily the one with the smallest sum of heights) 
from the point (0,0) to the point (n-1, m-1) and returns this height.

:param matrix: matrix, which is a representation of the terrain map. 
               Each value of the matrix corresponds to the elevation of the terrain at a given point on the map.
:param dictEdges: dictionary which contains the vertices and the corresponding lists of vertices to which they
                  are connected by an edge
:param dictIsVisited: dictionary that contains the vertices and their corresponding boolean values, which
                      store whether the node has already been visited (True) or not (False)
:param startRow: y-coordinate of starting point
:param startColumn: x-coordinate of starting point
:return height: the lowest height from the point (0,0) to the point (n-1, m-1)
'''
def minHeightPathInMap(matrix, dictEdges, dictIsVisited, startRow, startColumn):
    # n -> matrix column size
    n = len(matrix)
    # m -> matrix row size
    m = len(matrix[0])

    # minHeap -> heap which contains lists [value, x, y]
    #            WHERE:
    #               - value -> value of vertex
    #               - x -> x-coordinate of vertex
    #               - y -> y-coordinate of vertex
    #            All list are sorted by values (the smallest value will be popped first).
    minHeap = [[matrix[startRow][startColumn], startRow, startColumn]]

    dictIsVisited[(startRow, startColumn)] = True

    while minHeap is not []:
        height, row, col = heapq.heappop(minHeap)

        if row == n - 1 and col == m - 1:
            return height
        else:
            listOfNeigh = dictEdges.get((row, col))
            for i in listOfNeigh:
                if dictIsVisited.get(i):
                    continue
                dictIsVisited[i] = True
                x, y = i
                heapq.heappush(minHeap, [(max(height, matrix[x][y])), x, y])


matrix = [[1, 20, 24, 12, 12, 11], [2, 3, 2, 1, 0, 1], [7, 8, 5, 7, 6, 1], [2, 1, 4, 1, 3, 2],
          [1, 10, 15, 12, 15, 8], [0, 10, 20, 15, 13, 18], [0, 1, 1, 1, 13, 18], [3, 2, 5, 2, 1, 0]]
# matrix = [[1, 3, 1, 13], [0, 11, 1, 12], [0, 10, 1, 1], [0, 0, 4, 1]]

vertexex = addVertex(matrix)
edges = addEdge(matrix)
isVisited = addIsVisitedInfo(matrix)

print(minHeightPathInMap(matrix, edges, isVisited, 0, 0))
