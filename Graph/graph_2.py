class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict) 

    # Returns the paths can reach from start to end
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []

        paths = []
        for neighbor in self.graph_dict[start]:
            if neighbor not in path:
                new_paths = self.get_paths(neighbor, end, path)
                for p in new_paths:
                    paths.append(p)
        
        return paths

    # Returns the shortest path can reach from start to end
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        
        for neighbor in self.graph_dict[start]:
            if neighbor not in path:
                new_paths = self.get_shortest_path(neighbor, end, path)
                if (new_paths and not shortest_path) or len(new_paths) < len(shortest_path):
                    shortest_path = new_paths

        
        return shortest_path



routes = [
    ("MUM", "PAR"),
    ("MUM", "DUB"),
    ("PAR", "DUB"),
    ("PAR", "NYC"),
    ("DUB", "NYC"),
    ("NYC", "TOR")
]
route_graph = Graph(routes)

s = "MUM"
e = "NYC"
print(f"Paths between {s} to {e} is: ", route_graph.get_paths(s, e))
print("---------------------------------")
print(f"Shortest Paths between {s} to {e} is: ", route_graph.get_shortest_path(s, e))


# {'MUM': ['PAR', 'DUB'], 'PAR': ['DUB', 'NYC'], 'DUB': ['NYC'], 'NYC': ['TOR']}