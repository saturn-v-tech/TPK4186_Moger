# Task 4
# Class for Calculator


# 1 Packages
#-----------
from Task1 import *
from Task3 import *



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