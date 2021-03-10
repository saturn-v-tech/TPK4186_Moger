# Assignment 2 - TPK4186 - Assignment2 - Group 10# Lars Gruben and Torje Furu# 1. Imported packagesimport sysimport reimport matplotlib.pyplot as pltimport numpy as np# 2. Nodes# --------class Node:  def __init__(self, name):    self.name = name    self.arcs = []  def Get_Name(self):    return self.name  def Get_Arcs(self):    return self.arcs  def Add_Arcs(self,arc):    arcs = self.Get_Arcs()    arcs.append(arc)# 3. Arc# ------class Arc:  def __init__(self, node1, node2):    self.arc = []    self.arc.append(node1)    self.arc.append(node2)    # self.node1 = node1    # self.node2 = node2      # def __str__(self):  #   return self.node1.name + "-" + self.node2.name# 4. Graph# --------class Graph:  def __init__(self, graphName):    self.graphName = graphName    self.nodes = dict()    self.arcs = []  def Get_Name(self):    return self.graphName  def Get_Nodes(self):    return self.nodes  def Get_Node(self, name):    nodes = self.Get_Nodes()    nodeList = nodes.keys()    for nodeName in nodeList:       if nodeName == name:        return nodes[nodeName]    return None  def Get_Arcs(self):    return self.arcs  def Add_Node(self, nodeName):    node = Node(nodeName)    self.nodes[nodeName] = node    return node  def Add_Arc1(self, nodeName1, nodeName2):     node1 = self.nodes[nodeName1]    node2 = self.nodes[nodeName2]    arc = Arc(node1, node2)    arcs = self.arcs    arcs.append(arc)    node1.Add_Arcs(arc)    node2.Add_Arcs(arc)    return arc  def Add_Arc2(self, node1, node2):     # node1 = self.nodes[nodeName1]    # node2 = self.nodes[nodeName2]    arc = Arc(node1, node2)    arcs = self.arcs    arcs.append(arc)    node1.Add_Arcs(arc)    node2.Add_Arcs(arc)    return arc# # Canvas# class Canvas:#   def __init__(self):#     self.objects = []#   def New_Node(self, nodeName):#     node = Node(nodeName)#     self.objects.append(nodeName)#     return node#   def New_Arc(self, node1, node2):#     arc = Arc(node1, node2)#     self.arcs.append(arc)#     return arc#   def New_Graph(self, graphName):#     graph = Graph(graphName)#     self.objects.append(graph)#     return graphclass Printer:  def Graph_To_File(self, graph, outputFileName):    try:      outputFile= open(outputFileName, "w")    except:      sys.stderr.write("unable to write in file " + outputFileName + "\n")      sys.exit()    self.Graph(graph, outputFile)    outputFile.flush()    outputFile.close()  def Node(self, node, file):    nodeName = node.Get_Name()    file.write("\t" + nodeName)  def Arc(self, arc, file):    node1 = arc.arc[0]    node2 = arc.arc[1]    nodeName1 = node1.Get_Name()    nodeName2 = node2.Get_Name()    file.write("\t" + nodeName1 + "<->" + nodeName2)  def Graph(self, graph, file):    graphName = graph.Get_Name()    file.write("graph " + graphName + "\n")    nodesDictionary = graph.Get_Nodes()    nodes = nodesDictionary.values()    arcs = graph.Get_Arcs()    numberOfNodes = len(nodes)    numberOfArcs = len(arcs)    file.write("nodes\n")    count = 1    for node in nodes:       self.Node(node, file)      if count == numberOfNodes:        file.write(";\n")        break      else:        file.write(",")      if count%2!= 0:        count += 1      else:        file.write("\n")        count += 1    file.write("arcs\n")    count = 1    for arc in arcs:      self.Arc(arc, file)      if count == numberOfArcs:        file.write(";\n")        break      if count%3!= 0:        file.write(",")        count += 1      else:        file.write(",\n")        count += 1    file.write("end\n")class Parser:  def Import_File(self, inputFileName):    try:      inputFile = open(inputFileName, "r")    except:      sys.stderr.write("unable to open file " + inputFileName + "\n")      sys.exit()    graph = self.Read_File(inputFile)    inputFile.flush()    inputFile.close()    return graph  def Read_File(self, inputFile):    state = 0    for line in inputFile:      line = line.rstrip()      if re.match("graph", line):        words = line.split(" ")        graphName = words[1]        graph = Graph(graphName)      elif re.match("nodes", line):        state = 1      elif re.match("arcs", line):        state = 2      elif re.match("end", line):        break      elif state == 1:        nodes = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", line)        for node in nodes:          graph.Add_Node(node)      elif state == 2:        arcs = re.findall(r"([a-zA-Z0-9_])*\s*<->\s*([a-zA-Z0-9_]*)",line)        for arc in arcs:          nodeName1 = arc[0]          nodeName2 = arc[1]          node1 = graph.Get_Node(nodeName1)          node2 = graph.Get_Node(nodeName2)          graph.Add_Arc2(node1, node2)    return graph# 9. Calculatorclass Calculator:  def Degrees_Of_Nodes(self, graph):    degrees = dict()    nodeDict = graph.Get_Nodes()    arcList = graph.Get_Arcs()    listOfNames = nodeDict.keys()    # print(listOfNames)    #print(arcList)    for node in listOfNames:      degree = 0      for arc in arcList:        #print(arc)        node1 = arc.arc[0]        node2 = arc.arc[1]        name_node1 = node1.Get_Name()        name_node2 = node2.Get_Name()        # print(name_node1)        # print(name_node2)        if name_node1 == node or name_node2 == node:          degree += 1      degrees[node] = degree    return degrees  def Plot_Degrees(self, graph):    dictOfDegrees = self.Degrees_Of_Nodes(graph)    valuesOfDegrees = dictOfDegrees.values()    maxAmountOfDegrees = int(max(valuesOfDegrees))    plt.hist(valuesOfDegrees, bins = maxAmountOfDegrees + 1, range = (0, maxAmountOfDegrees + 1))    plt.title("Distribution of degrees")    plt.xlabel("Degrees")    plt.ylabel("# Nodes")    plt.xticks(np.arange(0, maxAmountOfDegrees + 1, 1))    plt.show()  def Node_Connected_Components(self, inputNode):    listOfConnectedComponents = [] # C    listOfCandidateNodes = [inputNode] # K    while len(listOfCandidateNodes) >= 1:      node = listOfCandidateNodes.pop(0)      listOfConnectedComponents.append(node)      arcList = graph.Get_Arcs()      for arc in arcList:        node1 = arc.arc[0]        node2 = arc.arc[1]        nodeName1 = node1.Get_Name()        nodeName2 = node2.Get_Name()        if nodeName1 == node:          if nodeName2 not in listOfConnectedComponents:            listOfConnectedComponents.append(nodeName2)        elif nodeName2 == node:          if nodeName1 not in listOfConnectedComponents:            listOfConnectedComponents.append(nodeName1)      return listOfConnectedComponents#   def Graph_Connected_Components(self, graph):# #     Add to the class Calculator a method to extract all the connected components of a# #     graph.#     listOfConnectedComponents = []#     nodesDict = graph.Get_Node()#     nodes = nodesDict.value()#     arcList = Graph.Get_Arcs()#     for node in nodes:#       connectedNodes = self.Node_Connected_Components(node)#       if node in connectedNodes:#         continue#       else:#         listOfConnectedComponents.append(node):#     return listOfConnectedComponents#   def DistributionOfConnectedLists(self, graph):#     listOfConnectedComponents = self.Graph_Connected_Components(graph)#     lengthOfList = []#     for components in listOfConnectedComponents:#       lengthOfList.append(len(components))#     return lengthOfList  #   def PlotConnectedComponentsDistribution(self, graph):#     lengthOfList = self.DistributionOfConnectedLists(graph)#     maxLength = max(len(lengthOfList))#     plt.hist(lengthOfList, bins = maxLength + 1, range = (0, maxLength + 1))#     plt.title("Distribution of degrees")#     plt.xlabel("Degrees")#     plt.ylabel("# Nodes")#     plt.xticks(np.arange(0, maxLength + 1, 1))#     plt.show()# Testsgraph = Graph("hallo")graph.Add_Node("A")graph.Add_Node("B")graph.Add_Node("C")graph.Add_Node("D")graph.Add_Node("E")graph.Add_Node("F")graph.Add_Node("G")graph.Add_Arc1("A","B")graph.Add_Arc1("B","C")graph.Add_Arc1("C","D")graph.Add_Arc1("A","E")graph.Add_Arc1("E","A")graph.Add_Arc1("F","A")# printer = Printer()# printer.Graph_To_File(graph, "TestGraph.tsv")# parser = Parser()# fileIn = parser.Import_File("TestGraph.tsv")# printer = Printer()# printer.Graph(fileIn, sys.stdout)# calculator = Calculator()# degrees = calculator.DegreesOfNodes(graph)# print(degrees)calculator = Calculator()nodeDegs = calculator.Degrees_Of_Nodes(graph)# calculator.Plot_Degrees(graph)print(nodeDegs)# node = "A"# conComp_Node = calculator.Node_Connected_Components(node)# print("Connected components (node ", node, "): ", conComp_Node)# conComp_Graph = calculator.Node_Connected_Components(graph)# print("Connected components (graph ", graph, "): ", conComp_Graph)