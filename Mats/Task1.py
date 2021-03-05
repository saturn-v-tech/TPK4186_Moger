#Task 1
#-------------


# 1 Node
#-------

class Node:
  def __init__(self, nodename):
    self.nodename = nodename
    self.nodes = []
    self.arcs = dict()

  def GetNode(self):
    return self.nodename
  def SetNode(self, nodename):
    self.nodename = nodename

  def GetArcs(self):
    return self.arcs.values()





# 2 Arcs
#-------

class Arcs(Node):
  def __init__(self):
    return
  
  def addArc(self, arcNumber, node1, node2):
    self.nodes.append(node1)
    self.nodes.append(node2)
    self.arcs[arcNumber] = [node1, node2]


# def NewArc(self, arcNumber, node1, node2):
  









  # def SetNode(self):
  #   self.node = node






a = Node("k1")
b = Node("k3")

print(a.nodename)

# print(Node.GetNode(b) + ' and ' + Node.GetNode(a))
# print(Nodes.self.values())







# Encode Edges
#-------------


  # class edges():
    








