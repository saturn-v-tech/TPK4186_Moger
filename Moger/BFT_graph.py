from collections import defaultdict

class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an egde to graph
    def addEgde(self, u, v):
        self.graph[u].append(v)

    # function to print a Breadth First Traversal of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it 
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from queue and print it 
            s = queue.pop(0)
            print(s, end = " ")

            # get all adjacent vertices of the dequeued vertex s. If adjacent has not been visited, then mark it visited an enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Driver code

# Create a graph given in the above diagram 
g = Graph()

g.addEgde(0, 1)
g.addEgde(0, 2)
g.addEgde(1, 2)
g.addEgde(2, 0)
g.addEgde(2, 3)
g.addEgde(3, 3)

print( "Following is Breadth First Traversal", '\n', 'starting from vertex 2')

g.BFS(2)