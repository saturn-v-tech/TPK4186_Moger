# Assignment 2


# 1 Imported packages
# --------------------

import sys
import re
import matplotlib.pyplot as plt
import random

# Task 1
# -------------

# 2 Class Node
# -------------

class Node:
  def __init__(self, nodeName):
    self.nodeName = nodeName
    self.arcs = []
    self.visited = False
    self.distance = 0
    self.degree = 0

  def GetNodeName(self):
    return self.nodeName

  def AddArc(self, arc):
    self.arcs.append(arc)

  def GetArcs(self):
    return self.arcs

  def GetVisited(self):
    return self.visited                                 #Visited funtions are used to not check nodes twice in ExtractConnectedComponentOfGraph function

  def SetVisited(self, value):
    self.visited = value

  def GetDistance(self):
    return self.distance

  def SetDistance(self, distance):                        #Distance functions and variable is used for task 9 and 10
    self.distance = distance

  def ResetDistance(self):
    self.distance = 0

  def SetDegree(self, degree):                          #Used to save the degree of a node and easy access in task 11 when degree is used for the probability
    self.degree = degree

  def GetDegree(self):
    return self.degree


# 2 Class Arcs
# -------------

class Arc:
  def __init__(self, node1, node2):
    self.node1 = node1
    self.node2 = node2
    # self.arc = [node1, node2]

  def GetArc(self):
    return self.node1, self.node2


# 3 Class Graph
# -------------

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

  def DeleteNode(self, nodeName):
    node = self.GetNode(nodeName)
    if node in self.nodes.values():
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

  def SetDegree(self, degree):                            #Added to access easy for task 11
    self.degree = degree

  def GetDegree(self):
    return self.degree


# Task 2:
# ----------------

# 4 Class Printer
# ----------------

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
  
  def PrintNodes(self, nodes, file):                   #Function for printing nodes on the format shown
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

  def PrintArcs(self, arcs, file):                      #Function for printing arcs on the format shown
    file.write('arcs')
    file.write('\n')
    count = 0
    lenArcs = 0
    for arc in arcs:
      if count == 0:                              #If count ==0, beginning of line and indent is added
        file.write('  ')
      if count <= 3:                                  # if count lower than 4, arc is added
        file.write(arc.node1.GetNodeName() + ' <-> ' + arc.node2.GetNodeName())
        count +=1
        lenArcs += 1
      if len(arcs) != lenArcs:         #As long as it's not the last arc, a comma is added
        file.write(', ')
      if count == 3:                    #New line for every 3 arc
        file.write('\n')
        count = 0
      elif len(arcs) == lenArcs:           #Last arc gets a ; to end
        file.write(';')

# Task 3
# --------------

# 5 Class Parser
# ---------------

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
      # print(newline)
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
        arcs = re.findall(r"([a-zA-Z0-9_]*)\s* <-> \s*([a-zA-Z0-9_]*)", line)       #Makes a list with the arcs sorert in a list of 2 nodes
        for arc in arcs:
          node1 = graph.GetNode(arc[0])
          node2 = graph.GetNode(arc[1])
          graph.NewArc(node1, node2)
    return graph

# Task 4
# ------------------

# 6 Class Calculator
# ------------------

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
    return nodeDegree                             #dictionary containing nodename and degree of node. outputprint is shown under tests


  def SetDegreeOfNodes(self, nodeDegree, inputGraph):                   #Making for easier excecution of task 11 so that the degree is saved in the Node
    nodeNames = list(nodeDegree.keys())
    for node in nodeNames:
      degree = nodeDegree[node]              #Every arc have two nodes. therefore the total degree of a graph is 2 times amount of arcs
      node = inputGraph.GetNode(node)
      node.SetDegree(degree)


  def SetDegreeOfGraph(self, inputGraph):
    arcs = inputGraph.GetArcs()
    degree = len(arcs)*2
    inputGraph.SetDegree(degree)  

  # Task 5
  # -------

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

  # Task 6
  # -------

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

  # Task 7 
  # -------

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

  # Task 7 
  # -------

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

  # Task 8
  # -------

  def PlotSizeDistributionOfConnectedComponentsOfGraph(self, graph):
    representedLengthComponents, numberOfLengthComponents = self.CalculateDistributionOfConnectedComponents(graph)
    plt.bar(representedLengthComponents, numberOfLengthComponents, width = 2)
    plt.xticks(representedLengthComponents)
    plt.yticks([i for i in range(1, max(numberOfLengthComponents)+1)])
    plt.xlabel('Number of connected components')
    plt.ylabel('Number of appearances')
    # plt.savefig('connectedComponentDistributionOfGraph.pdf')
    plt.show()

  # Task 9 
  # -------

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

  # Task 10 
  # -------

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

# Task 11 
# ----------------

# 7 Class Generator 
# -----------------

class Generator:

  def BarabasiGraph(self, graphName, size, NumberOfInitinalNodes):
    calculator = Calculator()
    graph = Graph(graphName)
    listNodeNames = list(range(1, size+1))
    for index in range(0, NumberOfInitinalNodes):                                               #Creating nodes in initial connected network
      graph.NewNode(str(listNodeNames[index]))
      listOfNodes = list(graph.GetNodes().values())                          #GetNodes returns dictionary with 'nodeName':node
    if NumberOfInitinalNodes < 2:
      return print('need number equal to 2 or higher')
    elif NumberOfInitinalNodes == 2:
      graph.NewArc(listOfNodes[0], listOfNodes[1])
    else:
      for i in range(0,NumberOfInitinalNodes-1):                           #Making  initial connected network consisting of m_0 nodes(NumberOfInitinalNodes)
        if i == 0:
          graph.NewArc(listOfNodes[i], listOfNodes[i+1])
          graph.NewArc(listOfNodes[i], listOfNodes[len(listOfNodes)-1])
        else:
          graph.NewArc(listOfNodes[i], listOfNodes[i+1])
    for index in range(NumberOfInitinalNodes, len(listNodeNames)):          #loop to get through the rest of the nodes that are not in the initial connected network
      newNode = graph.NewNode(str(listNodeNames[index]))
      nodes = graph.GetNodes().values()
      # calculator.CalculateDegreeOfNodes(graph)
      calculator.SetDegreeOfGraph(graph)
      for node in nodes:
        probability = node.GetDegree()/graph.GetDegree()
        if random.random()<probability:                       # If the probability is higher than the randomly made number, an arc is made between the newnode and existing nodes in graph
          graph.NewArc(newNode, node)
      if len(newNode.GetArcs()) == 0:
        graph.DeleteNode(newNode.nodeName)
    return graph



# Defining classes for use
# Nececcary for all testing --> leave uncommented
#-------------------------

printer = Printer()
parser = Parser()
calculator = Calculator()
generator = Generator()


#Task 12
#-------

# Nececcary values for testing, LEAV UNCOMMENTED
# To test the respective task uncomment the part under the marks
#----------------------------

NumberOfInitinalNodes = 2
testgraph = generator.BarabasiGraph('test1', 50, NumberOfInitinalNodes)             #Variables (graphName, size, NumberOfInitinalNodes)
graphName = testgraph.GetGraphName()
nodeNames = list(testgraph.GetNodes().keys())
arcs = testgraph.GetArcs()


#Print generated network
#-----------------------

# printer.PrintGraph(graphName, nodeNames, arcs, 'TestGeneratedGraph.txt')        #Print of generated networkf


#Parse generated network
#-----------------------

printer.PrintGraph(graphName, nodeNames, arcs, 'TestGeneratedGraph.txt') #Generating printed network for parsing
graph = parser.ImportGraph('TestGeneratedGraph.txt')         #Parsing Generated network
print(graph.GetGraphName())                                 # Showing print of what's read in from file
print(list(graph.GetNodes().keys()))
for arc in graph.GetArcs():
  print(arc.node1.GetNodeName(), arc.node2.GetNodeName())


#Verify a single connected component
#-----------------------------------

# def VerifyingSingleConnectedComponent(graph, NumberOfInitinalNodes):
#   graphConnectedList = calculator.ExtractConnectedComponentOfGraph(graph)      ##Outputlist containing lists of connected components(objects). If only one List, then they're all connected
#   if len(graphConnectedList) == 1:
#     print('netwotk is made of one single connected component')
#   else:
#     print('Network is NOT made of one singre connected component')


# VerifyingSingleConnectedComponent(testgraph, NumberOfInitinalNodes)       #Prints if the network is connected or not


#Extract and plot distribution of degree
#---------------------------------------

# calculator.PlotNodeDegreeDistritbution(testgraph)          #Makes plot and saves as pdf
# degrees = calculator.CalculateDegreeOfNodes(testgraph)
# print(degrees)                                                #Print of the variables (nodename:degree of node)


#Calculate diameter of netwotk
#-----------------------------

# diameter = calculator.CalculateDiameter(testgraph)            #Calculates diameter
# graphName = testgraph.GetGraphName()                            #Gets Name of graph
# print("The diameter of {0:s} is {1:d}".format(graphName,diameter))       #Prints variabl



