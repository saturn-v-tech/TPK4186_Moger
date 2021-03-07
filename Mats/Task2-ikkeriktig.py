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
    nodes = sorted(nodes)
    file.write('nodes \n')
    nodeindex = 1
    for node in nodes:
      if node[1] == str(nodeindex):
        if node[2] == str(1):
          file.write('  ' + node)                               #no comma on first node and indent
        else:
          file.write(', ' + node)
      else:
        file.write(',')
        nodeindex += 1
        file.write('\n')
        file.write('  ' + node)
    file.write(';')


  def PrintArcs(self, arcs, file):                   # assumed arcs is a dictionary grouped with arches at correct place as in test
    file.write('arcs')
    for arcline in arcs:
      firstInRow = True
      for arc in arcs[arcline]:
        if firstInRow:
          file.write('\n')
          file.write('  ')
          file.write(arc[0] + ' <-> ' + arc[1])
          firstInRow = False
        else:
          file.write(', ' + arc[0] + ' <-> ' + arc[1])
      if arcline == list(arcs.keys())[-1]:
        file.write(';')
      else:
        file.write(',')





# Test
printer = Printer()
nodes = ['n11', 'n12', 'n21', 'n22', 'n31', 'n32']
arcs = {1:[['n11', 'n12'], ['n11', 'n21'], ['n12', 'n22']], 2:[['n21', 'n22'], ['n21', 'n31'], ['n22', 'n32']], 3:[['n31', 'n32']]}    #number in dictionary is the line it belongs to

# printer.PrintNodes(nodes, sys.stdout)                      #Individual test Nodes
# printer.PrintArcs(arcs, sys.stdout)                        #Individual test Arcs
printer.PrintGraph('Grid32', nodes,arcs, sys.stdout)          #Test PrintGraph


# arc = arcs[1][1]
# print(arc)
# print(type(32))


# print(sorted(nodes1))


