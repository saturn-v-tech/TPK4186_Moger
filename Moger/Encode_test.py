

class AdjNode: 
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph: 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
        print(self.graph)

    # Function to add an edge in an undirected graph
    def add_arc(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        print(node.next)

        # Adding the source node to the destination as it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adj list of vertex {}\n head".format(i), end = "")
            temp = self.graph[i]
            while temp: 
                print(" <-> {}".format(temp.vertex), end = "")
                temp = temp.next
            print(' \n')

# Driver program to the above graph class 
graph = Graph(5) 

print(graph)

# graph.add_arc(0, 1) 

print(graph.add_arc(0, 1))

# graph.add_arc(0, 4) 
# graph.add_arc(1, 2) 
# graph.add_arc(1, 3) 
# graph.add_arc(1, 4) 
# graph.add_arc(2, 3) 
# graph.add_arc(3, 4) 
  
# graph.print_graph() 
