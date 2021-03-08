# Task 3
# Class for Parser


# 1 Packages
#-----------

import sys
from Task1 import *
import re



# 2 Class Parser
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




# Test
# parser = Parser()
# graph = parser.ImportGraph('ParserTest.txt')


# print(graph.GetGraphName())
# print(graph.GetNodes())
# print(graph.GetArcs())




















