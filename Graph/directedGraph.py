
'''
    a -> c
    |    |
    v    v
    b    e
    |
    v
    d -> f

'''

# METHOD 1: ITERATION
'''
def depthFirstSearch(graph, start):
    stack = [start]

    while len(stack) > 0:                           # OR while stack
        curr = stack.pop()
        print(curr)

        for neighbor in graph[curr]:
            stack.append(neighbor)
'''
'''
# METHOD 2: RECURSIVE
def depthFirstSearch(graph, start):
    print(start)
    for neighbor in graph[start]:
        depthFirstSearch(graph, neighbor)
'''

# METHOD 1: ITERATION
'''
def breadthFirstSearch(graph, start):
    queue = [start]
    while queue:
        curr = queue.pop(0)
        print(curr)

        for neighbor in graph[curr]:
            queue.append(neighbor)
'''

'''
Takes in an obj representing the adjacency list of a directed acyclic graph and two nodes
(start, dst). Returns boolean indicating whether or not there exists a directed path 
between the start and destination nodes.
'''
'''
def hasPath(graph, start, dst):
    if start == dst:
        return True

    for neighbor in graph[start]:
        if hasPath(graph, neighbor, dst):
            return True
    
    return False
'''
def hasPath(graph, start, dst):
    queue = [start]

    while queue:
        curr = queue.pop(0)

        if (curr == dst):
            return True

        for neighbor in graph[curr]:
            queue.append(neighbor)

    return False


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# depthFirstSearch(graph, 'a')
# breadthFirstSearch(graph, 'a')

print(hasPath(graph, 'c', 'f'))