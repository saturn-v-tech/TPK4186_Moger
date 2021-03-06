#Task 1
#-------------



#1 Node
#-------

class Nodes:
  def __init__(self, nodeName):
    self.nodeName = nodeName
    self.arcs = []

  def GetNode(self):
    return self.nodeName

  def SetNode(self, nodeName):
    self.nodeName = nodeName

  def GetArcs(self):
    return self.arcs

  def NewArc(self, arc):
    self.arcs.append(arc)


# 2 Arcs
#-------

class Arc:
  def __init__(self, node1, node2):
    self.arc = [node1, node2]

  def GetArc(self):
    return self.arc

  def SetArc(self, node1, node2):
    self.arc = [node1, node2]

#3 Graph
#------

class Graph:
  def __init__(self, graphName):
    self.graphName = graphName
    self.nodes = dict()
    self. arcs = []

  def GetGraphName(self):
    return self.graphName
  def SetGraphName(self, graphName):
    self.graphName = graphName

  def GetNodes(self):
    return self.nodes

  def NewNode(self, nodeName):
    newNode = Nodes(nodeName)
    self.nodes[nodeName] = newNode

  def DelNode(self, nodeName):
    del self.nodes[nodeName]

  def GetArcs(self):
    return self.arcs

  def NewArc(self, node1, node2):
    arc = Arc(node1, node2)
    self.arcs.append(arc)

  def GetNode(self, nodeName):
    nodes = self.GetNodes()
    nodenames = nodes.keys()
    if nodeName in nodenames:
      return nodeName
    else:
      return None




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
test.NewArc("Hei", "Hallo")
test.NewArc("morn", "Shalom")
test.NewNode(12)
test.DelNode(12)

# print(Graph.GetGraphName(test))
# print(Graph.GetNodes(test))
# print(Graph.GetArcs(test))

# print(test.GetNodes())
# print(test.GetArcs())
#




