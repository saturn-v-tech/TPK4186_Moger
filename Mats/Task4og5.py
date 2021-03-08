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


  def PlotNodeDegree(self, nodeDegrees):
    
    
    for keys in nodeDegrees:
      




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


nodeDegrees = calculator.CalculateDegreeOfNodes(graph)
calculator.PlotNodeDegree(nodeDegrees)