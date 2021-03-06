#Task 1
#-------------



#1 Node
#-------

class Node:
  def __init__(self, nodeName):
    self.nodeName = nodeName
    self.arcs = []
    self.visited = False
    self.distance = 0
    self.degree = 0

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

  def GetDistance(self):
    return self.distance

  def SetDistance(self, distance):
    self.distance = distance

  def ResetDistance(self):
    self.distance = 0

  def SetDegree(self, degree):                          #Used to save the degree of a node and easy access in task 11 when degree is used for the probability
    self.degree = degree

  def GetDegree(self):
    return self.degree



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
#------

class Graph:
  def __init__(self, graphName):
    self.graphName = graphName
    self.nodes = dict()
    self.arcs = []
    self.degree = 0

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

  def DeleteNode(self, nodeName):
    node = self.GetNode(nodeName)
    if node in self.nodes.values():
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

  def SetDegree(self, degree):
    self.degree = degree

  def GetDegree(self):
    return self.degree


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

node1 = test.NewNode("n11")
node2 = test.NewNode("n12")
node3 = test.NewNode("n21")
node4 = test.NewNode("n22")
node5 = test.NewNode("n31")
node6 = test.NewNode("n32")

arc1 = test.NewArc(node1, node2)
arc2 = test.NewArc(node3, node4)
arc3 = test.NewArc(node2, node4)

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

# test.DeleteNode('n22')
# print(test.GetNodes())
# print(test.GetArcs())
# print(test.nodes.get("n11"))

