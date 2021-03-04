"""
Task 1. Design:
– A class to encode nodes.
– A class to encode edges.
– A class to encore graphs.
The class to encode graphs should manage nodes and edges according to the factory design
pattern, i.e. that all nodes and edges must be created (and possibly deleted) via methods of
that class.
Test these classes by creating a small graph.
"""

# Graph class should hold a dict of nodes and a list of edges.

class Graph: 
    def __init__(self):
        pass

# Edges class will add edge in an undirected graph, both adding the node to the source node and adding the source node to the destination
# as it is the undirected graph.

class Edges: 
    def __init__(self):
        pass

    def add_edge(self, src, dest):
        node = Nodes(dest)
        node.next = Graph[src]

# Node class should  information about that node

class Nodes: 
    def __init__(self, data):
        self.node = data
        self.next = None

