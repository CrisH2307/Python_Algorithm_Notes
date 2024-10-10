'''
Write a function, connectedComponentsCount, that takes in the adjacency list of an undirected graph. 
The function should return the number of connected components within the graph.

'''

def connectedComponentsCount(graph):
    count = 0
    visited = set()
    for node in graph:
        print("Visiting: ", visited)
        if explore(graph, node, visited):
            count += 1
    return count

def explore(graph, curr, visited):
    if str(curr) in visited:
        return False

    visited.add(str(curr))

    for neighbor in graph[curr]:
        explore(graph, neighbor, visited)
    
    return True



print(connectedComponentsCount({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})); # -> 2
 

print(connectedComponentsCount({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})); # -> 1


print(connectedComponentsCount({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
})); # -> 5
