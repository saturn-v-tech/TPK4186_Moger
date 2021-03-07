# Task 2
# Class for printing a graph to a text file

# 1 packages
#-----------

import sys


#2 Printer
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
  
  
  



#Test
#----
printer = Printer()
nodes = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
arcs = [['a', 'b'], ['c', 'd'], ['c', 'd'], ['c', 'd'], ['a', 'b'], ['c', 'd'], ['c', 'd'], ['c', 'd']]
printer.PrintGraph('Grid32', nodes,arcs, sys.stdout)          #Test PrintGraph

# print(len(nodes))