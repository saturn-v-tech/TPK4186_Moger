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
        graphName = newline[0] # TODO skal denne være 0 eller 1? 
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


### TEST SECTION ### 

if __name__ == '__main__':

    parser = Parser()
    graph = parser.ImportGraph('ParserTest.txt')
    test = parser.ReadGraph('ParserTest.txt')

    # graph.DelNode('n11')
    # print(graph.GetGraphName())
    # print(graph.GetNodes())
    # print(graph.GetArcs())


    # a = graph.GetNode('n11')
    # b = a.GetArcs()
    # for arc in b:
    #   print(arc)
