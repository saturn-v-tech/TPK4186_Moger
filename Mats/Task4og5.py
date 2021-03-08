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
    nodes = inputGraph.GetNodes()
    arcs = inputGraph.GetArcs()
    for arc in arcs:                #arc is an object that can be accessed with either .arc which gieve [node1, node2] og .node1/.node2 that gives the individual node
      if nodeDegree.get(arc.node1, None) == None:
        nodeDegree[arc.node1] = 0
      if nodeDegree.get(arc.node2, None) == None:
        nodeDegree[arc.node2] = 0
      nodeDegree[arc.node1] += 1
      nodeDegree[arc.node2] += 1
    return nodeDegree                          #nodeDegree = {nodename:nodedegree, .....}


# Task 5
#-------


# 3 Plot degree of each node
#------------------------

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
    listApperance = []
    for i in range(1, maxDegree+1):
      NumberOfApperarance = Degrees.count(i)
      listApperance.append(NumberOfApperarance)
    plt.bar(listDegrees, listApperance)
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


calculator.PlotNodeDegreeDistritbution(graph)