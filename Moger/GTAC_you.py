class Graph: 
    def __init__(self, V, E):
        self.E = set(frozenset((u, v)) for  u, v in E) 
        self._nbrs = {}
        for v in V:
            self.addVertex(v)
        for u,v in self.E:
            self.addEgde(u, v)

    def addVertex(self, v):
        if v not in self._nbrs:
            self._nbrs[v] = set()

    def addEgde(self, u, v):
        self.E.add(frozenset([u, v]))
        self.addVertex(u)
        self.addVertex(v)
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)

    def removeEgde(self, u, v):
        e = frozenset([u, v])
        if e in self.E: 
            self.E.remove(e)
            self._nbrs[u].remove(v)
            self._nbrs[v].remove(u)

    def removeVertex(self, u):
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

    G.removeVertex(2)
    assert(G.n == 2 and G.m == 0)

    print("Okay")

