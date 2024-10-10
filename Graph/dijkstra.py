'''
- Finding Shortest Path from a fixed node to every other node.
Ex: Cities and routes between them
Step 1: Mark all nodes as unvisited
Visit = []
Unvisited = [A,B,C,D,E,F]
Step 2: Assign to all nodes a tentative distance value
    Node    Shortest Distance   Prev
    A               0
    B           INFINITY
    C
    D
    E
    F

Step 3: For a curr node, calculate the distance to all unvisited neighbours
Step 3.1: Update shortest distance, if new distance < old distance
Step 4: Mark curr node as visited
Step 5: Choose new curr node from unvisited notes with minimal distance
'''

class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacencies = []

    # Only add the adjancency if it's not already there
    # Assume other is already a vertex object
    def add_adjacency(self, other, weight):
        if other not in self.adjacencies:
        # if any(filter(lambda o: o[0] == other, self.adjacencies)):
            self.adjacencies.append((other, weight))
    
    def __str__(self):
        str_rep = "Node: " + str(self.data)
        return str_rep

class Graph:
    def __init__(self):
        self.verticies = set()

    # Assume that u and v are already Vertex obj
    def add_edge(self, u, v, weight):
        if u not in self.verticies:
            self.verticies.add(u)
        if v not in self.verticies:
            self.verticies.add(v)
        
        u.add_adjacency(v, weight)
        v.add_adjacency(u, weight)
    

    # Note: this implementation only gives you the distances, not
    # the paths themselves! 
    def dijkstra(self, start):
        # Set every distance to be infinity to start
        distances = {v: float('infinity') for v in self.verticies}

        # And then set the start distance to 0 (The start's distance from itself if 0)
        distances[start] = 0

        # Create a list that will minic a priority queue
        priority_queue = [(0, start)]

        while priority_queue:
            # Get the top of the priority queue
            curr_distance, curr_vertex = priority_queue.pop(0)

            # If our dist is somehow greater, move to next item in priority queue
            if curr_distance > distances[curr_vertex]:
                continue
            
            # Check all the adjacencies and their weights
            for neighbour, weight in curr_vertex.adjacencies:
                # Updating the distance to this curr node
                distance = curr_distance + weight

                # Checking if the node is now reachable faster via this new path
                if distance < distances[neighbour]:
                    # Update the distance
                    distances[neighbour] = distance 

                    # Prioritize this new path
                    priority_queue.insert(0, (distance, neighbour))

        return distances


graph = Graph()
a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')

# Connecting them in the graph
graph.add_edge(a, b, 1)
graph.add_edge(a, c, 4)
graph.add_edge(b, c, 2)
graph.add_edge(b, d, 5)
graph.add_edge(c, d, 1)

# Running the algorithms!
distances = graph.dijkstra(a)
for v in distances:
    print(f"The shortest distance from Node A to {v} is {distances[v]}")
#print("Minimum Spanning Tree Edges:", graph.prim_mst())