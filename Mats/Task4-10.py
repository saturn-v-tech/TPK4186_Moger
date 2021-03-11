# Task 4-8
#-------

# 1 Packages
#-----------
from Task1 import *
from Task3 import *
import matplotlib.pyplot as plt
import random


# 2 Class Calculator
#-------------------

# 2 Class Calculator
#-------------------

class Calculator:

  def CalculateDegreeOfGraph(self, inputGraph):
    nodeDegree = dict()
    arcs = inputGraph.GetArcs()
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
    self.SetDegreeOfNodes(nodeDegree, inputGraph)
    return nodeDegree
  

  def SetDegreeOfNodes(self, nodeDegree, inputGraph):                   #Making for easier excecution of task 11 so that the degree is saved in the Node
    nodeNames = list(nodeDegree.keys())
    for node in nodeNames:
      degree = nodeDegree[node]
      node = inputGraph.GetNode(node)
      node.SetDegree(degree)

  def SetDegreeOfGraph(self, inputGraph):
    arcs = inputGraph.GetArcs()
    degree = len(arcs)*2
    inputGraph.SetDegree(degree)

  def PlotNodeDegreeDistritbution(self, inputGraph):
    nodeDegrees = self.CalculateDegreeOfGraph(inputGraph)
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
    plt.savefig('NodeDegreeDristribution.pdf')
    plt.show()



  def ExtractConnectedComponentOfNode(self, node):
    nodeConnectedList = []                                               #list of connected components C
    candidateList = [node]                                           #List K of candidate nodes(objects, not names)
    while len(candidateList)>0:
        node = candidateList.pop(0)
        nodeConnectedList.append(node)
        NeighbourArcs = node.GetArcs()
        node.SetVisited(True)
        for arc in NeighbourArcs:
          node1 = arc.node1
          node2 = arc.node2
          if node == node1:
            if node2 not in nodeConnectedList and node2 not in candidateList:
              candidateList.append(node2)
          elif node == node2:
            if node1 not in nodeConnectedList and node1 not in candidateList:
              candidateList.append(node1)
    return nodeConnectedList



  def ExtractConnectedComponentOfGraph(self, graph):
    nodesDict = graph.GetNodes()
    nodes = nodesDict.values()
    graphConnectedList = []                                               #list of connected components C
    for node in nodes:
      if node.GetVisited():                                                     #node.GetVisited() returns true if the node is checked in ExtractConnectedComponentOfNode
        continue
      else:
        nodeConnectedList = self.ExtractConnectedComponentOfNode(node)
        graphConnectedList.append(nodeConnectedList)
    return graphConnectedList



  def CalculateDistributionOfConnectedComponents(self, graph):
    lengthConnectedComponents = dict()                                            #Dictionary with {lengh(number of connected components) : number of connected list with respective length}
    graphConnectedList = self.ExtractConnectedComponentOfGraph(graph)
    for connectedList in graphConnectedList:
      lengthInDictionary = lengthConnectedComponents.keys()
      lengthConnectedList = len(connectedList)
      if lengthConnectedList not in lengthInDictionary:
        lengthConnectedComponents[lengthConnectedList] = 1
      else:
        lengthConnectedComponents[lengthConnectedList] +=1
    representedLengthComponents = list(lengthConnectedComponents.keys())
    numberOfLengthComponents = list(lengthConnectedComponents.values())
    return representedLengthComponents, numberOfLengthComponents


  def PlotSizeDistributionOfConnectedComponentsOfGraph(self, graph):
    representedLengthComponents, numberOfLengthComponents = self.CalculateDistributionOfConnectedComponents(graph)
    plt.bar(representedLengthComponents, numberOfLengthComponents)
    plt.xticks(representedLengthComponents)
    plt.yticks([i for i in range(1, max(numberOfLengthComponents)+1)])
    plt.xlabel('Number of connected components')
    plt.ylabel('Number of appearances')
    # plt.savefig('connectedComponentDistributionOfGraph.pdf')
    plt.show()



  def CalculateDistance(self, sourceNode, graph):                         #May not need the graph input as long as node is already made as a part of a graph
    nodesDict = graph.GetNodes()
    nodes = nodesDict.values()
    for node in nodes:
      node.ResetDistance()                                       #Every node gets the distance 0 to start with
    treatedNodes = []                                               #list of treated components, C
    candidateList = [sourceNode]                                           #List K of candidate nodes(objects, not names)
    while len(candidateList)>0:
      node = candidateList.pop(0)
      treatedNodes.append(node)
      NeighbourArcs = node.GetArcs()
      for arc in NeighbourArcs:
        node1 = arc.node1
        node2 = arc.node2
        if node == node1:
          if node2 not in treatedNodes and node2 not in candidateList:
            newDistance = node.GetDistance() + 1
            node2.SetDistance(newDistance)
            candidateList.append(node2)
        elif node == node2:
          if node1 not in treatedNodes and node1 not in candidateList:
            newDistance = node.GetDistance() + 1
            node1.SetDistance(newDistance)
            candidateList.append(node1)
    return treatedNodes                                            #The treated nodes contains information about distance. By runnig the for loop in the test you may see the output


  def CalculateDiameter(self, graph):
    nodes = graph.GetNodes().values()
    diameter = 0
    for node in nodes:
      treatedNodes = calculator.CalculateDistance(node, graph)
      if diameter > len(treatedNodes):                             #No need to check distance if the amount of connected nodes is shorter than already discovered diameter
        continue
      distances = []
      for treatedNode in treatedNodes:
        distances.append(treatedNode.GetDistance())
      maxDistance = max(distances)
      if maxDistance > diameter:
        diameter = maxDistance
    return diameter



class Generator:

  def BarabasiGraph(self, graphName, size, NumberOfInitinalNodes):
    graph = Graph(graphName)
    listNodeNames = random.sample(range(1, size+1), size)
    for node in listNodeNames:                                               #Creating nodes in the graph
      graph.NewNode(node)
    listOfNodes = list(graph.GetNodes().values())                          #GetNodes returns dictionary with 'nodeName':node
    for i in range(0,NumberOfInitinalNodes-1):                           #Making  initial connected network consisting of m_0 nodes(NumberOfInitinalNodes)
      if i == 0:
        graph.NewArc(listOfNodes[i], listOfNodes[i+1])
        graph.NewArc(listOfNodes[i], listOfNodes[len(listOfNodes)-1])
      else:
        graph.NewArc(listOfNodes[i], listOfNodes[i+1])
    for index in range()




    # for node in graph.GetNodes().values():                          #GetNodes returns dictionary with 'nodeName':node
    #   print(node)



















#Test Calculator
#---------------

#Imported graph for testing
#--------------------------
parser = Parser()
graph = parser.ImportGraph('ParserTest.txt')     #Graph used for all tests. graph may be changed by adding/removing nodes and arcs in 'ParserTest.txt'



# Test of Calculator
#-------------------
calculator = Calculator()               #Nececcary for all testing. leave uncommented

# Test of CalculateDegreeOfGraph
#-------------------------------

#Output
#------
# degreeOfNodes = calculator.CalculateDegreeOfGraph(graph)
# print(degreeOfNodes)
# node = graph.GetNode('n12')
# print(node.GetDegree())

# Test of PlotNodeDegreeDistritbution
#-------------------------------


#Output
#------
# calculator.PlotNodeDegreeDistritbution(graph)


# Test of ExtractConnectedComponentOfNode
#----------------------------------------


#Output
#------
# node = graph.GetNode('n12')
# connectedList = calculator.ExtractConnectedComponentOfNode(node)
# for node in connectedList:
#   print(node.GetNodeName())


# Test of ExtractConnectedComponentOfGraph
#-----------------------------------------



#Output
#------
# graphConnectedList = calculator.ExtractConnectedComponentOfGraph(graph)
# for nodeConnectedList in graphConnectedList:
#   for node in nodeConnectedList:
#     print(node.GetNodeName())
#   print('\n')


# Test of PlotSizeDistributionOfGraph
#------------------------------------


#Output
#------
# calculator.PlotSizeDistributionOfConnectedComponentsOfGraph(graph)             #Plot


# Test of CalculateDistance
# --------------------------


#Output
#------
# node = graph.GetNode('n11')
# NodesWithDistance = calculator.CalculateDistance(node, graph)
# for node in NodesWithDistance:
#   print(node.GetNodeName(), node.GetDistance())


# Test of CalculateDiameter
# -------------------------



#Output
#------
# diameter = calculator.CalculateDiameter(graph)
# print(diameter)



# Generator
# ---------
generator = Generator()

# Test of Generator
# -----------------
generator.BarabasiGraph('test1', 20, 4)









