"""
Task 1. Design:
– A class to encode nodes.
– A class to encode edges.
– A class to encore graphs.
The class to encode graphs should manage nodes and edges according to the factory design
pattern, i.e. that all nodes and edges must be created (and possibly deleted) via methods of
that class.
Test these classes by creating a small graph.
"""

# 3. Graph class should hold a dict of nodes and a list of edges.

class Graph: 
    def __init__(self, V, E):
        self.E = set(frozenset((u, v)) for  u, v in E) 
        self._nbrs = {}
        for v in V:
            self.addNode(v)
        for u,v in self.E:
            self.addEgde(u, v)

    def addNode(self, v):
        if v not in self._nbrs:
            self._nbrs[v] = set()

    def addEgde(self, u, v):
        self.E.add(frozenset([u, v]))
        self.addNode(u)
        self.addNode(v)
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)

    def removeEgde(self, u, v):
        e = frozenset([u, v])
        if e in self.E: 
            self.E.remove(e)
            self._nbrs[u].remove(v)
            self._nbrs[v].remove(u)

    def removeNode(self, u):
        todelete = list(self.nbrs(u))
        for v in todelete:
            self.removeEgde(u, v)
        del self._nbrs[u]

    def deg(self, v):
        return len(self._nbrs[v])

    def nbrs(self, v):
        return iter(self._nbrs[v])

    @property
    def m(self):
        return len(self.E)

    @property
    def n(self):
        return len(self._nbrs)

# 1. Node class should  information about that node

class Nodes: 
    def __init__(self, nodeName):
        self.nodeName = nodeName

    def getNodeName(self):
        return self.nodeName

    def setNodeName(self, nodeName):
        self.nodeName = nodeName

    # Pretends data structure is supposed to hold information about people
    def getNodeData(self):
        return self.firstName, self.lastName, self.age, self.city

    def setNodeData(self, firstName, lastName, age, city): 
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.city = city

# 2. Egdes/Arcs class should hold the pair of nodes so the graphs class can encode the edges

class Edges:
    def __init__(self, nodeOne, nodeTwo):
        self.egdes = [nodeOne, nodeTwo]
    
    def getEdges(self):
        return self.egdes

    def setEgdes(self, nodeOne, nodeTwo):
        self.egdes = [nodeOne, nodeTwo]

N11 = Nodes('n11')
N12 = Nodes('n12')
N21 = Nodes('n21')
N22 = Nodes('n22')
N31 = Nodes('n31')
N32 = Nodes('n32')

Edges0 = Edges(N11, N12)
Edges1 = Edges(N11, N21)

if __name__ == '__main__':
    G = Graph({1, 2, 3}, {(1, 2), (2, 3)})
    assert(G.deg(1) == 1)
    assert(G.deg(2) == 2)
    assert(G.deg(3) == 1)
    assert(set(G.nbrs(2)) == {1, 3})
    assert(G.n == 3)
    assert(G.m == 2)
    
    G.removeEgde(1, 2)
    assert(G.n == 3 and G.m == 1)

    G.addEgde(1, 2)
    assert(G.n == 3 and G.m == 2)

    G.removeNode(2)
    assert(G.n == 2 and G.m == 0)

    print("Okay")
        


    




    



