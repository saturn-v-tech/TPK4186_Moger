# Task 5
# Class for Calculator


# 1 Packages
#-----------
from Task1 import *
from Task3 import *
import matplotlib.pyplot as plt


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
  


# Task 5
#-------
# Was insecure about what plot was requested, but assume PlotNodeDegreeDistritbution is the correct

# 3 Plot degree of each node
#---------------------------

  def PlotNodeDegree(self, inputGraph):
    nodeDegrees = self.CalculateDegreeOfNodes(inputGraph)
    nodeList = []
    degreeOfNodeList = []
    for node in nodeDegrees:
      nodeList.append(node)
      degreeOfNodeList.append(nodeDegrees[node])
    
    plt.barh(nodeList, degreeOfNodeList)
    plt.xlabel('Degree of Node')
    plt.ylabel('Node name')
    plt.show()


# 4 Plot distribution of the nodes og graph
#------------------------------------------

  def PlotNodeDegreeDistritbution(self, inputGraph):
    nodeDegrees = self.CalculateDegreeOfNodes(inputGraph)
    Degrees = list(nodeDegrees.values())
    maxDegree = max(Degrees)
    listDegrees = list(range(1, maxDegree+1))
    listDegreeApperance = []
    for i in range(1, maxDegree+1):
      NumberOfApperarance = Degrees.count(i)
      listDegreeApperance.append(NumberOfApperarance)
    plt.bar(listDegrees, listDegreeApperance)
    plt.xticks([i for i in range(1, maxDegree +1)])
    plt.xlabel('Degree of Node')
    plt.ylabel('Number of appearances')
    plt.show()



#Test
#----

#Imported graph for testing
#--------------------------
parser = Parser()
graph = parser.ImportGraph('ParserTest.txt')


# Test of Calculator
#-------------------
calculator = Calculator()
# calculator.CalculateDegreeOfNodes(graph)
# print(calculator.CalculateDegreeOfNodes(graph))

# calculator.PlotNodeDegree(graph)


# calculator.PlotNodeDegreeDistritbution(graph)