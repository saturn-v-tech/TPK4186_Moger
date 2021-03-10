# Task 6
#-------

# 1 Packages
#-----------
from Task1 import *
from Task3 import *
import matplotlib.pyplot as plt


# 2 Class Calculator
#-------------------

# 2 Class Calculator
#-------------------

class Calculator:

  def CalculateDegreeOfNodes(self, inputGraph):
    nodeDegree = dict()
    nodeList = inputGraph.GetNodes()
    arcs = inputGraph.GetArcs()
    nameList = nodeList.keys()
    for arc in arcs:                #arc is an object that can be accessed with either .arc which gieve [node1, node2] og .node1/.node2 that gives the individual node
      node1 = arc.node1
      node2 = arc.node2
      nodeName1 = node1.GetNodeName()
      nodeName2 = node2.GetNodeName()
      if nodeDegree.get(nodeName1, None) == None:
        nodeDegree[nodeName1] = 0
      if nodeDegree.get(nodeName2, None) == None:
        nodeDegree[nodeName2] = 0
      nodeDegree[nodeName1] += 1
      nodeDegree[nodeName2] += 1
    return nodeDegree
  

  def PlotNodeDegreeDistritbution(self, inputGraph):
    nodeDegrees = self.CalculateDegreeOfNodes(inputGraph)
    Degrees = list(nodeDegrees.values())
    maxDegree = max(Degrees)
    listDegrees = list(range(1, maxDegree+1))
    listDegreeApperance = []
    print(Degrees)
    for i in range(1, maxDegree+1):
      NumberOfApperarance = Degrees.count(i)
      listDegreeApperance.append(NumberOfApperarance)
    plt.bar(listDegrees, listDegreeApperance)
    plt.xticks([i for i in range(1, maxDegree +1)])
    plt.xlabel('Degree of Node')
    plt.ylabel('Number of appearances')
    plt.show()



  def ExtractConnectedComponentOfNode(self, node):
    connectedList = []                                               #list of connected components C
    candidateList = [node]                                           #List K of candidate nodes(objects, not names)
    while len(candidateList)>0:
      if candidateList[0] in connectedList:
        candidateList.pop(0)
      else:
        node = candidateList.pop(0)
        connectedList.append(node)
        NeighbourArcs = node.GetArcs()
        for arc in NeighbourArcs:
          node1 = arc.node1
          node2 = arc.node2
          if node == node1:
            if node2 not in connectedList:
              candidateList.append(node2)
          elif node == node2:
            if node1 not in connectedList:
              candidateList.append(node1)
    return connectedList







#Test
#----

#Imported graph for testing
#--------------------------
parser = Parser()
graph = parser.ImportGraph('ParserTest.txt')


# print(graph.GetNodes())

# Test of Calculator
#-------------------
calculator = Calculator()


# print(calculator.CalculateDegreeOfNodes(graph))
# calculator.PlotNodeDegreeDistritbution(graph)

# node = graph.GetNode('n11')
# nodeName = node.GetNodeName()
# arcs = node.GetArcs()
# print(arcs)

# node = Node('n12')
node = graph.GetNode('n51')

# calculator.ExtractConnectedComponentOfNode(node)





connectedList = calculator.ExtractConnectedComponentOfNode(node)
for node in connectedList:
  print(node.GetNodeName())







