# Terence Tong
# CSC 202 - 9
# files are formatted as such:
    # number of vertices
    # number of edges
    # edge connection(s)...
import unittest

# data point for the overall data structure of graph
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.visited = False

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __repr__(self):
        return 'Vertex({})'.format(self.id)


# collection of all vertices, Undirected meaning edges go both ways
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    # f and t are keys (ints)??
    def addEdge(self,f,t,cost=0):
        # print(f, t)
        # print(f in self.vertList)
        # print(self.vertList[f])
        if f not in self.vertList:
            nv = self.addVertex(f)
        # print(t not in self.vertList)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        # print(self.vertList[f])

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __repr__(self):
        return 'Graph({}, {})'.format(self.vertList, self.numVertices)


class MyGraph:

    # reads in the specification of a graph and creates a graph using an
    # adjacency list representation. You may assume the graph is not empty and is a correct specification.
    # E.g. each edge is represented by a pair of vertices between 1 and n. Note that the graph is not directed
    # so each edge specified in the input file should appear on the adjacency list of each vertex of the two
    # vertices associated with the edge.
    def __init__(self, filename):
        file = open(filename, 'r', encoding='utf-8-sig')
        self.graph = Graph()
        firstRun = True
        for line in file:
            _line = line.strip('\n').split()
            if firstRun and len(_line) == 1:
                firstRun = False
                for i in range(1, int(_line[0]) + 1):
                    self.graph.addVertex(i)
                    # print(self.graph.vertList[i])
            elif len(_line) == 2:
                # because its an undirected graph
                self.graph.addEdge(int(_line[0]), int(_line[1]))
                self.graph.addEdge(int(_line[1]), int(_line[0]))
        file.close()


    # returns a list of lists. For example, if there are three connected
    # components then you will return a list of three lists. The order of the sub-lists is not important.
    # However each sub-list will contain the vertices (in ascending order) in the connected component
    # represented by that list. Each vertex is represented by an integer from 1 to n. If a vertex has no edges it
    # will be in a connected component containing only itself.
    # None -> list of lists
    def conn_components(self):
        num_visited = 0
        i = 1
        output = []
        while num_visited < len(self.graph.vertList):
            if self.graph.vertList[i].visited is False:
                output.append(self.dfs(i))
            num_visited += 1
            i += 1
        return output

    # starting key for the depth first search
    # returns a sorted list of all things visited
    # int -> list of ints
    def dfs(self, key):
        stack = [self.graph.vertList[key]]
        output = []
        while len(stack) != 0:
            v = stack.pop()
            if v.visited is False:
                v.visited = True
                output.append(v.id)
                for vert in v.connectedTo:
                    stack.append(vert)
        return sorted(output)

    def __repr__(self):
        return self.graph.__repr__()

# class MyTestCase(unittest.TestCase):
#     def test_1(self):
#         t = MyGraph('test_graph1.txt')
#         self.assertEqual(t.conn_components(), [[1,2,3,4,5],[6,7,8,9]])
#
#     def test_2(self):
#         t = MyGraph('test_graph3.txt')
#         self.assertEqual(t.conn_components(), [[1, 2, 3], [4, 6, 7, 8], [5]])
#
# if __name__ == '__main__':
#     unittest.main()