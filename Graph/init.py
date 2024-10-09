class Vertex:
    def __init__(self, data):
        self.data = data
        self.adjacencies = []

    # Only add the adjacency if it's not already there
    # Assume other is already in the adjacencies
    def add_adjacency(self, other, weight):
        if other not in self.adjacencies:
            self.adjacencies.append((other, weight))

class Graph:
    # Initializing an empty graph
    def __init__(self):
        self.verticies = set()

    def add_edge(self, u, v, weight):
        if u not in self.verticies:
            self.verticies.append(u)
        if v not in self.verticies:
            self.verticies.append(v)

        # Since this is undirected graph
        u.add_adjacency(v, weight)
        v.add_adjacency(u, weight)