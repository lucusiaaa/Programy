class Graph:

    """
    Constructor of the Graph class
    """
    def __init__(self):
        self.dictionaryWithEdges = {}
        self.dictionaryWithDegree = {}

    '''
    This function adding edge between two vertices (ver1, ver2) to dictionary containing all vertices
    and the corresponding lists of vertices to which they are connected by an edge.
    '''
    def addEdge(self, ver1, ver2):
        tempList = self.dictionaryWithEdges.get(ver1)
        tempList.append(ver2)
        self.dictionaryWithEdges[ver1] = tempList
        tempNum = self.dictionaryWithDegree.get(ver2)
        tempNum += 1
        self.dictionaryWithDegree[ver2] = tempNum

    '''
    This function adding vertex (ver) to dictionary containing all vertices
    and the corresponding lists of vertices to which they are connected by an edge
    (at the beginning it is set as []).
    '''
    def addVertex(self, ver):
        self.dictionaryWithEdges[ver] = []
        self.dictionaryWithDegree[ver] = 0

    '''
    A topological sort is a non-unique permutation of the nodes of a directed graph such that 
    an edge from u to v implies that u appears before v in the topological sort order. 
    This ordering is valid only if the graph has no directed cycles.
    
    :return: list with vertices where for every directed edge uv from vertex u to vertex v, 
    u comes before v in the ordering.
    '''
    def topologicalSort(self):
        # sortedList -> the list in which the sorted elements will be stored
        sortedList = []
        # queue -> an auxiliary data structure storing vertices that do not have
        #          an in-degree edges
        queue = []
        # dictInDegree -> dictionary with all vertices and the corresponding number
        #                 of in-degree edges
        dictInDegree = self.dictionaryWithDegree.copy()

        for i in dictInDegree:
            if dictInDegree.get(i) == 0:
                queue.append(i)

        while queue:
            tempVer = queue.pop(0)
            sortedList.append(tempVer)
            for i in self.dictionaryWithEdges.get(tempVer):
                temp = dictInDegree.get(i)
                temp -= 1
                dictInDegree[i] = temp
                if temp == 0:
                    queue.append(i)

        return sortedList


graph = Graph()

graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)


graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(3, 4)
graph.addEdge(3, 5)
graph.addEdge(4, 5)
graph.addEdge(2, 4)

# graph.addVertex("A")
# graph.addVertex("B")
# graph.addVertex("C")
# graph.addVertex("D")
# graph.addVertex("E")
# graph.addVertex("F")
# graph.addVertex("G")
# graph.addVertex("H")
# graph.addVertex("I")
# graph.addVertex("J")
# graph.addVertex("K")
#
# graph.addEdge("A", "B")
# graph.addEdge("A", "C")
# graph.addEdge("A", "D")
# graph.addEdge("B", "J")
# graph.addEdge("C", "F")
# graph.addEdge("C", "I")
# graph.addEdge("D", "G")
# graph.addEdge("D", "E")
# graph.addEdge("E", "K")
# graph.addEdge("E", "H")

print(graph.dictionaryWithEdges)
print(graph.topologicalSort())
