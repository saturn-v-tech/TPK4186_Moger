# Task 4-8
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


  def CalculateDistance(self, node, graph):                         #May not need the graph input as long as node is already made as a part of a graph
    treatedNodes = []                                               #list of treated components, C
    candidateList = [[node, 0]]                                           #List K of candidate nodes(objects, not names)
    print(candidateList[0])
    

    while len(candidateList)>0:
      node = candidateList[0].pop(0)
      print(node)
      # treatedNodes.append(node)
      # NeighbourArcs = node.GetArcs()
      # print(node)
    #   for arc in NeighbourArcs:
    #     print(arc)
    # print(sourceNode)







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

# Test of ExtractConnectedComponentOfNode
#----------------------------------------
# node = graph.GetNode('n11')
# calculator.ExtractConnectedComponentOfNode(node)

# connectedList = calculator.ExtractConnectedComponentOfNode(node)
# for node in connectedList:
#   print(node.GetNodeName())


# Test of ExtractConnectedComponentOfGraph
#-----------------------------------------

# graphConnectedList = calculator.ExtractConnectedComponentOfGraph(graph)
# for nodeConnectedList in graphConnectedList:
#   for node in nodeConnectedList:
#     print(node.GetNodeName())
#   print('\n')


# Test of PlotSizeDistributionOfGraph
#------------------------------------

# calculator.PlotSizeDistributionOfConnectedComponentsOfGraph(graph)


# Test of CalculateDistance
# --------------------------
node = graph.GetNode('n12')

calculator.CalculateDistance(node, graph)




