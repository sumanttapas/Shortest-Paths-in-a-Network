# OSPF_Dijsktras: The program implement's an OSPF protocol using Dijkstra's algorithm to find the
#              shortest path between vertices. It also calculates reachable vertices from any given vertex in the graph.
# Arguments: The program needs 1 argument, Name of the text file which has the initial condition of the graph.
# Author:   Sumant Sanjay Tapas
# UNCC ID:  800905142
# Email ID: stapas@uncc.edu


import sys
from sys import argv


# Function Implements minHeapify. The input arguments are list A which needs to be heapified, index i and length of the
# list A.
def minHeapify(A, i, n):
    l = left(i)
    r = right(i)
    if l <= n and A[l][0] < A[i][0]:
        smallest = l
    else:
        smallest = i
    if r <= n and A[r][0] < A[smallest][0]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        minHeapify(A, smallest, n)


# This function builds a min heap. Input list A, and size of list A.
def buildMinHeap(A, n):
    for i in range(int(n/2)-1, -1, -1):
        minHeapify(A, i, n-1)


# Inserts a new element in the priority Queue.
# Input Arguments: List A, New element key
def insert(A, ele):
    A.insert(len(A), ele)
    buildMinHeap(A, len(A))


# This function changes the priority of an element in a min heap.
# Input Arguments: List A, index of the element of which the priority needs to be changed i, New value key
def decreasePriority(A, i, key):
    A[i] = key
    while i > 0 and A[parent(i)][0] > A[i][0]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


# Extracts the min value from the priority queue.
# Input Arguments: List A
def extractMin(A):
    minimum = A[0]
    A[0] = A[len(A)-1]
    del A[len(A)-1]
    minHeapify(A, 0, (len(A) - 1))
    return minimum[1]


def left(i):
    return 2*i+1


def parent(i):
    if i % 2 == 0 and i != 0:
        return int((i/2)-1)
    elif i % 2 != 0:
        return int(i/2)
    else:
        return 0


def right(i):
    return 2*i+2


# Holds all the properties of a vertex
class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.dist = sys.maxsize
        self.prev = None
        self.status = 1

    def reset(self):
        self.dist = sys.maxsize
        self.prev = None


# Holds all the properties of an edge
class Edge:
    def __init__(self, destination, weight):
        self.vertex = destination
        self.weight = weight
        self.status = 1


# Holds all the properties of a graph. Most complicated class in the program.
# Major functions are: shortestPath()- to find the shortest path between the two given vertices.
#                      reachable()- Prints all the vertices reachable from any vertex in the graph
#                      printGraph()- Prints every vertex in the graph with its corresponding edges and weights.
class Graph:


    vertexMap = {}  # dictionary which holds all the vertex objects.

    # returns a vertex object using an input argument as name of the vertex.
    # If the vertex is not present a vertex object is created
    def getVertex(self, vertexName):
        if vertexName not in self.vertexMap:
            v = Vertex(vertexName)
            self.vertexMap.update({vertexName: v})
            return v
        else:
            return self.vertexMap[vertexName]

    def getAddedVertex(self, vertexName):
        if vertexName in self.vertexMap:
            return self.vertexMap[vertexName]
        else:
            return -1

    def addEdgeIni(self, source, destination, weight):
        v = self.getVertex(source)
        w = self.getVertex(destination)
        edgeVtoW = Edge(w, float(weight))
        edgeWtoV = Edge(v, float(weight))
        v.adj.insert(len(v.adj), edgeVtoW)
        w.adj.insert(len(w.adj), edgeWtoV)

    # Adds an edge from source to destination with the weight as passed in the input arguments.
    def addEdge(self, source, destination, weight):
        v = self.getVertex(source)
        w = self.getVertex(destination)
        for ver in v.adj:
            if ver.vertex == w:
                ver.weight = float(weight)
                ver.status = 1
                return
        edge = Edge(w, float(weight))
        v.adj.insert(len(v.adj), edge)

    # Deletes an edge from source to destination.
    def deleteEdge(self, source, destination):
        v = self.getAddedVertex(source)
        w = self.getAddedVertex(destination)
        if v != -1 and w != -1:
            for ver in v.adj:
                if ver.vertex == w:
                    v.adj.remove(ver)
                    # self.vertexMap.update({v.name: v})
                    return
        else:
            if v != -1:
                print("Source Vertex not found")
            elif w != -1:
                print("Destination Vertex not found")

    # Makes the edge from source to destination down.
    def edgeDown(self, source, destination):
        v = self.getAddedVertex(source)
        w = self.getAddedVertex(destination)
        if v != -1 and w != -1:
            for edge in v.adj:
                if edge.vertex == w:
                    edge.status = 0
                    return
        else:
            if v != -1:
                print("Source Vertex not found")
            elif w != -1:
                print("Destination Vertex not found")

    # Makes the edge from source to destination up.
    def edgeUp(self, source, destination):
        v = self.getAddedVertex(source)
        w = self.getAddedVertex(destination)
        if v != -1 and w != -1:
            for edge in v.adj:
                if edge.vertex == w:
                    edge.status = 1
                    return
        else:
            if v != -1:
                print("Source Vertex not found")
            elif w != -1:
                print("Destination Vertex not found")

    # Makes the vertex passed as  input parameter 'vertex' down.
    def vertexDown(self, vertex):
        v = self.getAddedVertex(vertex)
        if v != -1:
            v.status = 0
        else:
            print("Vertex not found")

    # Makes the vertex passed as  input parameter 'vertex' down.
    def vertexUp(self, vertex):
        v = self.getAddedVertex(vertex)
        if v != -1:
            v.status = 1
        else:
            print("Vertex not found")

    # Function prints the path to a destination passed as an input argument. This function is called when the shortest
    # algorithm is completed.
    def printPath(self, destination):
        v = self.getVertex(destination)
        if v.dist == sys.maxsize:
            print("Destination is not reachable..!!")
        else:
            # print("Distance is:", v.dist)
            self.printPathV(v)
            print(" ", end="")
            print("%.2f" % v.dist)

    # Recursive helper function of printPath function.
    def printPathV(self, vertex):
        if vertex.prev != None:
            self.printPathV(vertex.prev)
            print(" ", end="")
        print(vertex.name, end="")

    def getWeight(self, vertexA, vertexB):
        for element in vertexA.adj:
            if element.vertex == vertexB:
                return element.weight

    # Prints the current position/condition of the graph
    def printGraph(self):
        ver = list(self.vertexMap.values())
        listver = []
        for item in ver:
            listver.insert(len(listver), item.name)    # check if only active vertices needs to printed or not
        listver.sort()
        for item in listver:
            v = self.getAddedVertex(item)
            if v.status == 0:
                print(v.name, "DOWN")
            else:
                print(v.name)
            listver1 = []
            weightList = {}
            for item1 in v.adj:
                listver1.insert(len(listver1), (item1.vertex.name, item1))
                weightList.update({item1.vertex.name: item1.weight})
            # listver1.sort()
            for item2 in listver1:
                w = self.getAddedVertex(item2[0])
                print(" ", w.name, end="")
                print(" ", end="")
                if item2[1].status == 0:
                    print(weightList[w.name], end="")
                    print(" DOWN")
                else:
                    print(weightList[w.name])

    def clearAll(self):
        for vertex in self.vertexMap.values():
            vertex.reset()

    # Implements Dijkstras algorithm to calculate shortest path. Input argument is the source vertex's name.
    def shortestPath(self, source):
        self.clearAll()
        v = self.getVertex(source)  # get the vertex object of the source.
        v.dist = 0  # set the distance of the vertex as 0.
        q = []
        for w in self.vertexMap:
            q.insert(len(q), (self.vertexMap[w].dist, self.vertexMap[w]))
        buildMinHeap(q, len(q))  # build a binary min heap for the priority queue
        s = []
        while q:
            v = extractMin(q)  # extract the minimum distance element from the priority queue
            if v.status == 0:  # if the vertex is not active, skip the vertex
                continue
            else:
                s.insert(len(s), v)  # marked the vertex as visited
                for element in v.adj:  # for each element in the adjacency list of vertex v,
                    if element.vertex not in s and element.status == 1 and element.vertex.status == 1:  # if the edge and vertex is active
                        prevDistance = element.vertex.dist
                        if element.vertex.dist > v.dist + self.getWeight(v, element.vertex):  # if the current distance is greater than the distance of weight and prev distance change the distance and prev vertex
                            element.vertex.dist = v.dist + self.getWeight(v, element.vertex)
                            element.vertex.prev = v
                            index = q.index((prevDistance, element.vertex))
                            decreasePriority(q, index, (element.vertex.dist, element.vertex))  # change the priority of the vertex as the distance is now changed.

    # Prints all reachable vertices from all the vertices of the graph. It implements a DFS like algorithm for
    # each vertex. The time complexity of the algorithm in O(V*(V+E)).
    def reachable(self):
        ver = list(self.vertexMap.values())
        listver = []
        for item in ver:
            if item.status == 1:
                listver.insert(len(listver), item.name)
        listver.sort()  # step is to only arrange the vertices in an alphabetical order.
        listver2 = []
        for item1 in listver:
            w = self.getAddedVertex(item1)
            listver2.insert(len(listver2), w.name)
            print(w.name)  # print the current vertex name
            marked = []
            validPath = self.printValidPath(w, listver2, marked)  # recursively call this function until all the vertices are visited
            listver2.clear()
            validPath.sort()  # sort to print in alphabetical order.
            for name in validPath:
                print(" ", name)
            validPath.clear()  # clear this list to make it ready for the next vertex

    # Helper function for reachable
    def printValidPath(self, vertex, visited, marked1):
        for edge in vertex.adj:
            if edge.status == 1:
                v = edge.vertex
                if v.name not in visited and v.status == 1:
                    visited.insert(len(visited), v.name)
                    marked1.append(v.name)
                    self.printValidPath(v, visited, marked1)
        return marked1

# Main function starts from here.
# Program reads a file provided as an input argument and constructs a graph.
# Ask's user for the input query and perform subsequent actions on the graph.

g = Graph()
fileobj = open(argv[1], "r")   # Opens the file which contains the initial graph.
for line in fileobj:
    node = line.split()
    if len(node) != 3:
        print("Ill formatted Line ", end="")
        print(node)
        exit()
    else:
        g.addEdgeIni(node[0], node[1], float(node[2]))  # Adds an edge from each vertex of the graph.
fileobj.close()
print("File read...")
print(len(g.vertexMap), "vertices present in the graph")  # Prints the number of vertices in the graph.
while True:
    inputstr = input("\nQuery: ")  # Get the input query from the user.
    query = inputstr.split()
    if len(query) == 3:
        if query[0] == "path":
            if query[1] not in g.vertexMap.keys():
                print("Source Vertex Not found")
            else:
                g.shortestPath(query[1])
            if query[2] not in g.vertexMap.keys():
                print("Destination Vertex Not found")
            else:
                g.printPath(query[2])
        elif query[0] == "deleteedge":
            g.deleteEdge(query[1], query[2])
        elif query[0] == "edgedown":
            g.edgeDown(query[1], query[2])
        elif query[0] == "edgeup":
            g.edgeUp(query[1], query[2])
        else:
            print("Invalid Command, Please try again")
    elif len(query) == 2:
        if query[0] == "vertexdown":
            g.vertexDown(query[1])
        elif query[0] == "vertexup":
            g.vertexUp(query[1])
        else:
            print("Invalid Command, Please try again")
    elif len(query) == 1:
        if query[0] == "print":
            g.printGraph()
        elif query[0] == "quit":
            break
        elif query[0] == "reachable":
            g.reachable()
        else:
            print("Invalid Command, Please try again")
    elif len(query) == 4:
        if query[0] == "addedge":
            g.addEdge(query[1], query[2], query[3])
        else:
            print("Invalid Command, Please try again")
    else:
        print("Wrong Command. Please try again")
