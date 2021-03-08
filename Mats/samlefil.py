#Assignment 2


# 1 Imported packages
#--------------------

import sys
import re


#Task 1
#-------------

#2 Node
#-------

class Nodes:
  def __init__(self, nodeName):
    self.nodeName = nodeName
    self.arcs = []

  def GetNode(self):
    return self.nodeName

  def SetNode(self, nodeName):
    self.nodeName = nodeName

  def GetArcs(self):
    return self.arcs

  def NewArc(self, arc):
    self.arcs.append(arc)


# 3 Arcs
#-------

class Arc:
  def __init__(self, node1, node2):
    self.arc = [node1, node2]

  def GetArc(self):
    return self.arc

  def SetArc(self, node1, node2):
    self.arc = [node1, node2]

#4 Graph
#------

class Graph:
  def __init__(self, graphName):
    self.graphName = graphName
    self.nodes = dict()
    self. arcs = []

  def GetGraphName(self):
    return self.graphName
  def SetGraphName(self, graphName):
    self.graphName = graphName

  def GetNodes(self):
    return self.nodes

  def NewNode(self, nodeName):
    newNode = Nodes(nodeName)
    self.nodes[nodeName] = newNode

  def DelNode(self, nodeName):
    del self.nodes[nodeName]

  def GetArcs(self):
    return self.arcs

  def NewArc(self, node1, node2):
    arc = Arc(node1, node2)
    self.arcs.append(arc)

  def GetNode(self, nodeName):
    nodes = self.GetNodes()
    nodenames = nodes.keys()
    if nodeName in nodenames:
      return nodeName
    else:
      return None


#5 Printer
#---------

class Printer:
  
  
  def PrintGraph(self, graphName, nodes, arcs, file):
    file.write('graph' + '\t' + str(graphName))
    file.write('\n')
    Printer.PrintNodes(self, nodes, file)
    file.write('\n')
    Printer.PrintArcs(self, arcs, file)
    file.write('\n')
    file.write('end')
  
  def PrintNodes(self, nodes, file):           #nodes are assuned format (n11, n21)correct input. sorts if not sorted
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
        file.write(arc[0] + '<->' + arc[1])
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
      file = open(filename,'r')
    except:
      sys.stderr.write("Unable to open file " + filename + "\n")
      sys.exit()
      
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
        arcs = re.findall(r"([a-zA-Z0-9_][0-9]*\s*[<=>]*\s*[a-zA-Z0-9_][0-9]*)", line)
        for arc in arcs:
          arc = arc.split('<=>')
          node1 = arc[0]
          node2 = arc[1]
          graph.NewArc(node1, node2)
    return graph






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
# printer = Printer()
# nodes = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# arcs = [['a', 'b'], ['c', 'd'], ['c', 'd'], ['c', 'd'], ['a', 'b'], ['c', 'd'], ['c', 'd'], ['c', 'd']]
# printer.PrintGraph('Grid32', nodes,arcs, sys.stdout)          #Test PrintGraph

#Test Parser
#-----------
parser = Parser()
graph = parser.ImportGraph('ParserTest.txt')

print(graph.GetGraphName())
print(graph.GetNodes())
print(graph.GetArcs())
