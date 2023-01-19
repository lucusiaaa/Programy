'''
This function returns the lowest cost path in the graph as a list and sum of all elements in those list

:param dictVertices: dictionary which contains the vertices and their corresponding values in the matrix
:param dictEdges: dictionary which contains the vertices and the corresponding lists of vertices to which they
                  are connected by an edge
:param dictIsVisited: dictionary that contains the vertices and their corresponding boolean values, which
                      store whether the node has already been visited (True) or not (False)
:param start: initial point
:return minList, minSum: the lowest cost path in the graph as a list and sum of all elements in those list
'''
def findBestPath(dictVertices, dictEdges, dictIsVisited, start):
    # Jeśli aktualny węzeł jest ostatnim to go zwróć
    if start == len(dictVertices) - 1:
        resList = [start]
        # zwraca listę z węzłem i sumę
        return resList, dictVertices.get(start)

    # minList - list with the lowest cost path in the graph
    minList = None
    # minSum - sum of all elements in minList
    minSum = None

    # Ustaw aktualny jako odwiedzony
    # isVisited - copy of dictIsVisited
    isVisited = dictIsVisited.copy()
    isVisited[start] = True

    # listAllNeighbours - list of all neighbours to visit for the 'start' vertex
    listAllNeighbours = dictEdges[start]

    # listPossibleNeigh - list of neighbours that could be visited
    listPossibleNeigh = []
    for i in listAllNeighbours:
        if not dictIsVisited[i]:
            listPossibleNeigh.append(i)

    for i in listPossibleNeigh:
        resList, sum = findBestPath(dictVertices, dictEdges, isVisited, i)
        if sum is not None and minSum is None:
            minSum = sum
            minList = resList.copy()
        if sum is not None and minSum > sum:
            minSum = sum
            minList = resList.copy()
    if minSum is None:
        return None, None
    else:
        minSum += dictVertices.get(start)
        minList.append(start)

    # Jeśli nie ma sąsiadów (martwy punkt) i aktualny węzęł nie jest ostatnim
    if listPossibleNeigh == [] and start != len(dictVertices):
        return None, None

    return minList, minSum


'''
This function create dictionary containing all vertices and info if a vertex 
has already been visited during a graph search.

:param matrix: matrix, which is a representation of the terrain map. 
               Each value of the matrix corresponds to the elevation of the terrain at a given point on the map.
:return dictionaryWithIsVisited: dictionary containing all vertices and info if vertex has already been visited 
                                 during a graph search.
'''
def addIsVisitedInfo(matrix):
    dictionaryWithIsVisited = {}
    for i in range(len(matrix) * len(matrix[0])):
        dictionaryWithIsVisited[i] = False
    return dictionaryWithIsVisited


'''
This function create dictionary containing all vertices and the corresponding lists of 
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
                listOfNeigh.append(j + (i - 1) * len(matrix))
            # Adding bottom neighbour
            if i != len(matrix) - 1:
                listOfNeigh.append(j + (i + 1) * len(matrix))
            # Adding left neighbour
            if j != 0:
                listOfNeigh.append((j - 1) + i * len(matrix))
            # Adding right neighbour
            if j != len(matrix[i]) - 1:
                listOfNeigh.append((j + 1) + i * len(matrix))

            dictionaryWithEdges[j + i * len(matrix)] = listOfNeigh
    return dictionaryWithEdges

'''
This function create dictionary containing all vertices with corresponding values.

:param matrix: matrix, which is a representation of the terrain map. 
               Each value of the matrix corresponds to the elevation of the terrain at a given point on the map.
:return: dictionary which contains the vertices and their corresponding values in the matrix
'''
def addVertex(matrix):
    dictionaryWithVertexes = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            dictionaryWithVertexes[j + i * len(matrix)] = matrix[i][j]

    return dictionaryWithVertexes


# matrix = [[1, 4, 1, 3], [5, 2, 2, 3], [4, 1, 5, 2], [2, 3, 3, 5]]
matrix = [[1, 1, 11, 1, 1, 1], [11, 1, 11, 1, 11, 1], [11, 1, 11, 1, 11, 1], [11, 1, 11, 1, 11, 1],
          [11, 1, 11, 1, 11, 1], [11, 1, 1, 1, 11, 1]]
numOfVertex = len(matrix) * len(matrix[0])

vertexex = addVertex(matrix)
edges = addEdge(matrix)
isVisited = addIsVisitedInfo(matrix)

print(vertexex)
print(edges)
print(vertexex.keys())
print(isVisited)
print()
print(findBestPath(vertexex, edges, isVisited, 0))
