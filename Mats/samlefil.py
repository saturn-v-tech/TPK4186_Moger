#Assignment 2


# 1 Imported packages
#--------------------



#Task 1
#-------------

#2 Node
#-------

class Nodes:
  def __init__(self, nodeName):
    self.nodeName = nodeName
    self.arcs = []

  def GetNode(self):
    return self.nodeName

  def SetNode(self, nodeName):
    self.nodeName = nodeName

  # def GetArcs(self):
  #   return self.arcs.values()




#3 Arcs
#-------

class Arc:
  def __init__(self, node1, node2):
    self.arc = []
  
  def addArc(self, node1, node2):
    self.nodes.append(node1)
    self.nodes.append(node2)
    self.arcs.append([node1, node2])




#4 Graph
#------

class Graph:
  def __init__(self, graphName):
    self.nodes = dict()
    self. arcs = []
    


