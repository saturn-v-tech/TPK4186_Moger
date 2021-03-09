# https://www.youtube.com/watch?v=uFaZY1dVnGs
# GTAC 2.6: Implementing a Graph Data Structure in Python 

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

if __name__ == '__main__':
    G = Graph(
        {'n11', 'n12', 'n21', 'n22', 'n31', 'n32'}, 
        {('n11', 'n12'), 
        ('n11', 'n21'), 
        ('n12', 'n22'), 
        ('n21', 'n22'), 
        ('n21', 'n31'), 
        ('n22', 'n32'), 
        ('n31', 'n32')})
    assert(G.deg('n11') == 2) # number of deg for specific node
    assert(G.deg('n12') == 2) # number of deg for specific node
    assert(G.deg('n21') == 3) # number of deg for specific node
    assert(set(G.nbrs('n32')) == {'n31', 'n22'}) # check nbrs 
    assert(G.n == 6) # number of nodes
    assert(G.m == 7) # number of edges
    
    G.removeEgde('n11', 'n21')
    assert(G.n == 6 and G.m == 6) # number of nodes and edges

    G.addEgde('n31', 'n11')
    assert(G.n == 6 and G.m == 7) # number of nodes and edges

    G.removeNode('n31')
    assert(G.n == 5 and G.m == 4) # number of nodes and edges 

    print("Okay")

