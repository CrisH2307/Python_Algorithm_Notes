
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



graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# depthFirstSearch(graph, 'a')
breadthFirstSearch(graph, 'a')