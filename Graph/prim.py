# MST: Prim
'''
What is Minimun Spanning Tree (MST)?
- Given an undirected graph with weighted edges, a Minimum Spanning Tree is a subset
of the edges in the graph which connects all vertices together (without creating any cycles)
while minimizing the total edge cost.


Prim's MST Algorithm
- Is a greedy algorithm that works well on dense graphs. On these graphs, Prim's meets or 
improves on the time bounds of its popular rivals (Kruskal's & Boruvka's).
- However, when it comes to finding the minimum spanning forest on a disconnected graph, 
Prim cannot do this as easily (the algorithm must be run on each connected component individually).
- The lazy version of Prim's has a run time of O(e log e), but the eager version 
has a better runtime of O(e log v)

Lazy Algorithm:
- Maintain a min Priority Queue that sorts edges based on min edge cost. This will be used
to determine the next node to visit and the edge used to get there.
- Start the algorithm on any node (s). Mark (s) as visited and iterate over all edges of (s),
adding them to the Priority Queue
- While the PQ is not empty and a MST has not been formed, dequeue the next cheapest edge from the
PQ. If the dequeued edge is outdated (meaning the node it points to has already been visited) 
then skip it and poll again. Otherwise, mark the current node as visited and add the selected
edge to the MST.
- Iterate over the new current node's edges and add all its edges to the PQ. Do not add
edges to the PQ which point to already visited nodes.

*** One thing to bear in mind is that although the graph above represents an undirected graph,
the internal adjacency list representation typically has each undirected edge stored as two directed edges.


PSUDO COde:
n = ... # Number of nodes in graph
pq = ... # Priority Queue stores edge objects consisting of {start, end, cost} tuples. The PQ sorts
           edges based on min edge cost.
g = ... # Graph representing an adjacency list of weighted edges. Each undirected edge is represented as
          two directed edges in g. For especially dense graphs, prefer using an adjacency matrix instead
          of an adjacency list to improve performance
visited = [false] * n # visited i tracks whether node i has been visited; size n

'''
import heapq

class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost  

def prim_mst(graph, start=0):
    n = len(graph)
    mst_cost = 0
    edge_count = 0
    mst_edges = []

    visited = [False] * n
    pq = []

    def add_edges(node_index):
        visited[node_index] = True
        for edge in graph[node_index]:
            if not visited[edge.to]:
                heapq.heappush(pq, edge)

    add_edges(start)

    while pq and edge_count < n - 1:
        edge = heapq.heappop(pq)
        
        if visited[edge.to]:
            continue
        
        mst_edges.append(edge)
        mst_cost += edge.cost
        edge_count += 1
        add_edges(edge.to)

    if edge_count != n - 1:
        return None, None

    return mst_cost, mst_edges


# Example graph initialization and function call:
# Define graph as adjacency list where graph[u] contains Edge instances to other nodes.
graph = [
    [Edge(1, 4), Edge(2, 1)],  # edges from node 0
    [Edge(0, 4), Edge(2, 3), Edge(3, 2)],  # edges from node 1
    [Edge(0, 1), Edge(1, 3), Edge(3, 5)],  # edges from node 2
    [Edge(1, 2), Edge(2, 5)]  # edges from node 3
]

mst_cost, mst_edges = prim_mst(graph)
print("Minimum Spanning Tree Cost:", mst_cost)
for edge in mst_edges:
    print(f"Edge from {edge.to} with cost {edge.cost}")