'''
This function returns True when in the list of neighbours all vertices have been previously visited.
:param listWithNeigh: list of all neighbours to visit for the vertex
:param dictionaryWithIsVisited: dictionary containing all vertices and info if vertex has already been visited
                                during a graph search.
:return: boolean
'''


def checkVertexList(listWithNeigh, dictionaryWithIsVisited):
    for i in listWithNeigh:
        if not dictionaryWithIsVisited.get(i):
            return False
    return True


'''
This function returns True if all vertices were visited.
:param dictionaryWithIsVisited: dictionary containing all vertices and info if vertex has already been visited 
                                during a graph search.
:return: boolean
'''


def checkIfAllVisited(dictionaryWithIsVisited):
    for i in dictionaryWithIsVisited:
        if not dictionaryWithIsVisited.get(i):
            return False
    return True


class Graph:
    # Constructor of the Graph class
    def __init__(self):
        self.numOfVertexes = 0
        self.numOfEdges = 0
        self.dictionaryWithEdges = {}

    '''
    This function adding edge between two vertices (ver1, ver2) to dictionary containing all vertices
    and the corresponding lists of vertices to which they are connected by an edge.
    '''
    def addEdge(self, ver1, ver2):

        tempList = self.dictionaryWithEdges.get(ver1)
        tempList.append(ver2)
        self.dictionaryWithEdges[ver1] = tempList
        self.numOfEdges += 1

    '''
    This function adding vertex (ver) to dictionary containing all vertices
    and the corresponding lists of vertices to which they are connected by an edge
    (at the beginning it is set as []).
    '''
    def addVertex(self, ver):
        self.dictionaryWithEdges[ver] = []
        self.numOfVertexes += 1

    '''
    This function create dictionary containing all vertices and info if a vertex
    has already been visited during a graph search.
    :return: dictionary <vertex: boolean>
    '''
    def createIsVisitedInfo(self):
        dictionaryWithIsVisited = {}
        listOfKeys = self.dictionaryWithEdges.keys()
        for i in listOfKeys:
            dictionaryWithIsVisited[i] = False
        return dictionaryWithIsVisited

    '''
    This function is a frontend method for recursive call of topologicalSortRecursive().

    :return: list with vertices where for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
    '''
    def topologicalSort(self):
        resList = []
        finalList = []
        dictIsVisited = self.createIsVisitedInfo()
        tempList = self.topologicalSortRecursive(resList, dictIsVisited, self.dictionaryWithEdges.copy())

        for i in range(self.numOfVertexes - 1):
            finalList.append(tempList[self.numOfVertexes - i - 1])

        return finalList

    '''
    This function is a recursive function of topologicalSort().

    :param resList: list containing results of ordering
    :param dictIsVisited: dictionary containing info if vertices've been visited
    :param dictionaryWithEdges: dictionary containing all vertices with list of neighbours 
    :return: list containing results of ordering
    '''
    def topologicalSortRecursive(self, resList, dictIsVisited, dictionaryWithEdges):

        if checkIfAllVisited(dictIsVisited):
            return resList
        temp = dictionaryWithEdges.copy()
        for k in temp:
            listWithNeigh = dictionaryWithEdges.get(k)
            if listWithNeigh == [] or checkVertexList(listWithNeigh, dictIsVisited):
                resList.append(k)
                dictIsVisited[k] = True
                dictionaryWithEdges.pop(k)
        self.topologicalSortRecursive(resList, dictIsVisited, dictionaryWithEdges)
        return resList


graph = Graph()

# graph.addVertex(1)
# graph.addVertex(2)
# graph.addVertex(3)
# graph.addVertex(4)
# graph.addVertex(5)
#
# graph.addEdge(1, 3)
# graph.addEdge(1, 4)
# graph.addEdge(3, 4)
# graph.addEdge(3, 5)
# graph.addEdge(4, 5)
# graph.addEdge(2, 4)

graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")
graph.addVertex("G")
graph.addVertex("H")
graph.addVertex("I")
graph.addVertex("J")
graph.addVertex("K")

graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("A", "D")
graph.addEdge("B", "J")
graph.addEdge("C", "F")
graph.addEdge("C", "I")
graph.addEdge("D", "G")
graph.addEdge("D", "E")
graph.addEdge("E", "K")
graph.addEdge("E", "H")

print(graph.dictionaryWithEdges)
print(graph.topologicalSort())
