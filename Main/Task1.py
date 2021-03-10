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


# 2 Arcs
#-------

class Arc:
  def __init__(self, node1, node2):
    self.node1 = node1
    self.node2 = node2
    # self.arc = [node1, node2]

  def GetArc(self):
    return self.node1, self.node2


#3 Graph
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

  def NewArc(self, node1, node2):
    arc = Arc(node1, node2)
    self.arcs.append(arc)
    node1.AddArc(arc)
    node2.AddArc(arc)
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
    
    # Test nodes
    #-----------

    # a = Node("hei")
    # b = Node("morna")

    # delNode = Node.GetNode(a)

    # print(delNode)

    # print("Okay")


# Test nodes
#-----------

# a = Nodes("hei")
# b = Nodes("morna")

# delNode = Nodes.GetNode(a)

# print(delNode)

# Test arc
#---------

# a = Arc('hei', 'hade')
# print(Arc.GetArc(a))

# Test graph
#-----------

test = Graph("testGraph")

# node1 = test.NewNode("n11")
# node2 = test.NewNode("n12")
# node3 = test.NewNode("n21")
# node4 = test.NewNode("n22")
# node5 = test.NewNode("n31")
# node6 = test.NewNode("n32")

# arc1 = test.NewArc(node1, node2)
# arc2 = test.NewArc(node3, node4)
# arc3 = test.NewArc(node2, node4)

# print(node1.GetArcs())



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