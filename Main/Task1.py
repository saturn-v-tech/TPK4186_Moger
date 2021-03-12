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
# A class to encode nodes
#-------

class Node:
  def __init__(self, nodeName):
    self.nodeName = nodeName
    self.arcs = []
    self.visited = False

  def GetNodeName(self):
    return self.nodeName

  def AddArc(self, arc):
    self.arcs.append(arc)

  def GetArcs(self):
    return self.arcs

  def GetVisited(self):
    return self.visited

  def SetVisited(self, value):
    self.visited = value


# A class to encode arcs
#-------

class Arc:
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest
    self.arc = [src, dest]

  def GetArc(self):
    return self.arc 


# A class to encode graphs
#-------

class Graph:
  def __init__(self, graphName):
    self.graphName = graphName
    self.nodes = dict()
    self.arcs = []

  def GetGraphName(self):
    return self.graphName

  def SetGraphName(self, graphName):
    self.graphName = graphName

  def GetNodes(self):
    return self.nodes

  def NewNode(self, nodeName):
    node = Node(nodeName)
    self.nodes[nodeName] = node
    return node

  def DelNode(self, nodeName):
    del self.nodes[nodeName]

  def GetArcs(self):
    return self.arcs

  def NewArc(self, src, dest):
    arc = Arc(src, dest)
    self.arcs.append(arc)
    src.AddArc(arc)
    dest.AddArc(arc)
    return arc

  def GetNode(self, nodeName):
    nodes = self.GetNodes()
    nodenames = nodes.keys()
    if nodeName in nodenames:
      return self.nodes[nodeName]
    else:
      return None

### TEST SECTION ### 

if __name__ == '__main__':

    ### Initialize 

    test = Graph("testGraph")

    node1 = test.NewNode("n11")
    node2 = test.NewNode("n12")
    node3 = test.NewNode("n21")
    node4 = test.NewNode("n22")
    node5 = test.NewNode("n31")
    node6 = test.NewNode("n32")

    arc1 = test.NewArc(node1, node2)
    arc2 = test.NewArc(node1, node3)
    arc3 = test.NewArc(node3, node4)
    arc4 = test.NewArc(node2, node4)

    # Node

    assert node1.GetNodeName() == 'n11'
    assert node6.GetNodeName() == 'n32'

    # Arc

    print(test.GetArcs())

    print('okay')

    # node2 = Node('n12')
    # arcs = test.GetArcs()
    # node2.NewNeighbourArc(arcs[0])
    # node2.NewNeighbourArc(arcs[2])
    # a = node2.GetNeigbourArcs()
    # print(node1.arcs)



    # print(Graph.GetGraphName(test))
    # print(test.GetNodes())
    # print(test.GetNode('a'))
    # print(test.GetArcs())

    # print(test.GetNodes())
    # print(test.GetArcs())


"""
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

"""