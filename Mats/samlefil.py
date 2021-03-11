#Assignment 2


# 1 Imported packages
#--------------------

import sys
import re
import matplotlib.pyplot as plt
import random

#Task 1
#-------------

#2 Node
#-------

class Node:
  def __init__(self, nodeName):
    self.nodeName = nodeName
    self.arcs = []
    self.visited = False
    self.distance = 0

  def GetNodeName(self):
    return self.nodeName

  def AddArc(self, arc):
    self.arcs.append(arc)

  def GetArcs(self):
    return self.arcs

  def GetVisited(self):
    return self.visited

  def SetVisited(self, value):
    self.visited = value

  def GetDistance(self):
    return self.distance

  def SetDistance(self, distance):
    self.distance = distance

  def ResetDistance(self):
    self.distance = 0


# 2 Arcs
#-------

class Arc:
  def __init__(self, node1, node2):
    self.node1 = node1
    self.node2 = node2
    # self.arc = [node1, node2]

  def GetArc(self):
    return self.node1, self.node2


#3 Graph
#------

class Graph:
  def __init__(self, graphName):
    self.graphName = graphName
    self.nodes = dict()
    self.arcs = []

  def GetGraphName(self):
    return self.graphName

  def SetGraphName(self, graphName):
    self.graphName = graphName

  def GetNodes(self):
    return self.nodes

  def NewNode(self, nodeName):
    node = Node(nodeName)
    self.nodes[nodeName] = node
    return node

  def DelNode(self, nodeName):
    del self.nodes[nodeName]

  def GetArcs(self):
    return self.arcs

  def NewArc(self, node1, node2):
    arc = Arc(node1, node2)
    self.arcs.append(arc)
    node1.AddArc(arc)
    node2.AddArc(arc)
    return arc

  def GetNode(self, nodeName):
    nodes = self.GetNodes()
    nodenames = nodes.keys()
    if nodeName in nodenames:
      return self.nodes[nodeName]
    else:
      return None


#5 Printer
#---------

class Printer:
  
  
  def PrintGraph(self, graphName, nodes, arcs, OutputFile):
    try:
      file= open(OutputFile, "w")
    except:
      sys.stderr.write("unable to write in file " + OutputFile + "\n")
      sys.exit()
    file.write('graph' + '\t' + str(graphName))
    file.write('\n')
    Printer.PrintNodes(self, nodes, file)
    file.write('\n')
    Printer.PrintArcs(self, arcs, file)
    file.write('\n')
    file.write('end')
    file.flush()
    file.close()
  
  def PrintNodes(self, nodes, file):
    count = 1
    file.write('nodes \n')
    for nodeName in nodes:
      if count%2 == 1:
        file.write('  ' + nodeName)
        count +=1
      else:
        file.write(', ')
        file.write(nodeName)
        if len(nodes) != count:
          file.write(',')
          file.write('\n')
        else:
          file.write(';')
        count +=1


  def PrintArcs(self, arcs, file):
    file.write('arcs')
    file.write('\n')
    count = 0
    lenArcs = 0
    for arc in arcs:
      if count == 0:
        file.write('  ')
      if count <= 3:
        file.write(arc[0] + ' <-> ' + arc[1])
        count +=1
        lenArcs += 1
      if len(arcs) != lenArcs:
        file.write(', ')
      if count == 3:
        file.write('\n')
        count = 0
      elif len(arcs) == lenArcs:
        file.write(';')

# 6 Class Parser
#---------------

class Parser:

  def ImportGraph(self, filename):
    try:
      file = open(filename, "r")
    except:
      sys.stderr.write("unable to open file " + filename + "\n")
      sys.exit()
    graph = self.ReadGraph(file)
    file.flush()
    file.close()
    return graph


  def ReadGraph(self, file):
    state = 0
    firstline = True
    
    for line in file:
      newline = line.split()
      if firstline:
        graphName = newline[1]
        graph = Graph(graphName)
        firstline = False
      elif re.match('nodes', line) != None:
        state = 1
      elif re.match('arcs', line) != None:
        state = 2
      elif re.match('end', line) != None:
        break 
      elif state == 1:
        nodes = re.findall(r"[a-zA-Z0-9_][0-9]*", line)
        for node in nodes:
          graph.NewNode(node)
      elif state == 2:
        arcs = re.findall(r"([a-zA-Z0-9_][0-9]*\s*[<=>\t]*\s*[a-zA-Z0-9_][0-9]*)", line)
        for arc in arcs:
          arc = arc.split(' <=> ')                            #splits and gets the two nodes separated. May be improved by making it more general and not rely too much upon exact input with spaces etc
          node1 = graph.GetNode(arc[0])
          node2 = graph.GetNode(arc[1])
          graph.NewArc(node1, node2)
    return graph


# 7 Class Calculator
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
    self.SetDegreeOfNodes(nodeDegree, inputGraph)
    return nodeDegree              #dictionary containing nodename and degree of node. outputprint is shown under tests



  def SetDegreeOfNodes(self, nodeDegree, inputGraph):                   #Making for easier excecution of task 11 so that the degree is saved in the Node
    nodeNames = list(nodeDegree.keys())
    for node in nodeNames:
      degree = nodeDegree[node]
      node = inputGraph.GetNode(node)
      node.SetDegree(degree)


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
    return nodeConnectedList                                                 #Output is a list of nodes(objects) that are connected. prit of names are shown under test (output)



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
    return graphConnectedList                                              #Outputlist containing lists of connected components(objects). To see the output with names of nodes, run the for loop mentioned under tests



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
    plt.bar(representedLengthComponents, numberOfLengthComponents, width = 2)
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
    return diameter                                                #Output a number. print shown in tests





# Defining classes for use
#-------------------------
printer = Printer()
parser = Parser()
calculator = Calculator()               #Nececcary for all testing. leave uncommented


# Test graph
#-----------

# test = Graph("testGraph")

# node1 = test.NewNode("n11")
# node2 = test.NewNode("n12")
# node3 = test.NewNode("n21")
# node4 = test.NewNode("n22")
# node5 = test.NewNode("n31")
# node6 = test.NewNode("n32")

# arc1 = test.NewArc(node1, node2)
# arc2 = test.NewArc(node3, node4)
# arc3 = test.NewArc(node2, node4)


# print(Graph.GetGraphName(test))
# print(test.GetNodes())
# print(test.GetNode('a'))
# print(test.GetArcs())
# 
# print(test.GetNodes())
# print(test.GetArcs())


#Test Printer
#------------
# nodes = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# arcs = [['a', 'b'], ['c', 'd'], ['c', 'd'], ['c', 'd'], ['a', 'b'], ['c', 'd'], ['c', 'd'], ['c', 'd']]
# printer.PrintGraph('Grid32', nodes,arcs, 'tesst.txt')          #Test PrintGraph


#Test Parser
#-----------
graph = parser.ImportGraph('ParserTest.txt')                    # Used for all tasks

# print(graph.GetGraphName())
# print(graph.GetNodes())
# print(graph.GetArcs())


#Test Calculator
#---------------

#Imported graph for testing
#--------------------------
# graph = parser.ImportGraph('ParserTest.txt')



# Test of Calculator
#-------------------


# Test of CalculateDegreeOfNodes
#-------------------------------

#Output
#------
# print(calculator.CalculateDegreeOfNodes(graph))


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
calculator.PlotSizeDistributionOfConnectedComponentsOfGraph(graph)             #Plot


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



