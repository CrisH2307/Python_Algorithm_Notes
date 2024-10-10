'''
    i - j
    | /   
    k - l
    |
    m

    o --- n
'''
def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())


def hasPath(graph, start, dst, visited):
    if start == dst:
        return True

    if start in visited:
        return False
    visited.add(start)
    
    for neighbor in graph[start]:
        if hasPath(graph, neighbor, dst, visited):
            return True
    
    return False

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
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirectedPath(edges, 'j', 'm'))

graph = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}