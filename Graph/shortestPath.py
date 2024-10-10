'''
Write a function, shortestPath, that takes in an array of edges for an undirected graph
and two nodes (nodeA, nodeB). The function should return the length of the shortest path 
between A and B. Consider the length as the number of edges in the path, not the number 
of nodes. If there is no path between A and B, then return -1. You can assume that A and 
B exist as nodes in the graph.
'''

def shortestPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    visited = set([nodeA])
    queue = [[nodeA, 0]]

    while queue:
        [node, dist] = queue.pop(0)
        if node == nodeB:
            return dist
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, dist + 1])

    return -1

def buildGraph(edges):
    graph = {}

    for edge in edges:
        [a, b] = edge
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)

    return graph

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
];

print(shortestPath(edges, 'e', 'c')) # -> 2
