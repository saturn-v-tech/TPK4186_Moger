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
      graph = Parser.ReadGraph(file)
      return graph





  def ReadGraph(self, filename):
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
          node = graph.NewNode(node)
      elif state == 2:
        arcs = re.findall(r"([a-zA-Z0-9_][0-9]*)", line)
        print(arcs)
    



    # print(graph.GetNodes())





    # print(graph.GetGraphName())









# Test
parser = Parser()
parser.ReadGraph('ParserTest.txt')
