'''
Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output: [0, 2, 3, 1, 4]
Explanation: Starting from 0, the BFS traversal will follow these steps: 
Visit 0 → Output: 0 
Visit 2 (first neighbor of 0) → Output: 0, 2 
Visit 3 (next neighbor of 0) → Output: 0, 2, 3 
Visit 1 (next neighbor of 0) → Output: 0, 2, 3, 
Visit 4 (neighbor of 2) → Final Output: 0, 2, 3, 1, 4

--- Psudo code
2 args
BFS(G, s):   g-graph ; s-source node
    Q is queue
    Q enqueue(s) // ínsertinf s in queue until all its neightbour will be visited now
        
    make visited false for len of the adj
        
    mark s as visited = true
        
    while q not empty:
        //Removing that vertex from queue,whose neighbour will be visited now
        v = q.deque()
            
        for all neightbour weight of verticies in Graph g:
            if w is not visited:
                Q.enqueue(w)
                mark w as visited
        

BFS(graph, start):
    Create an empty list called result
    Create a visited list of size equal to number of vertices, all set to False
    Create an empty queue

    Enqueue start
    Mark start as visited

    While queue is not empty:
        Dequeue a node and call it current
        Add current to result

        For each neighbor in graph[current]:
            If neighbor is not visited:
                Enqueue neighbor
                Mark neighbor as visited

    Return result


------
1 arg
BFS(graph):
    Create an empty list called result
    Create a visited list of size equal to number of vertices, all set to False
    Create an empty queue

    Enqueue the starting node (0)
    Mark starting node as visited

    While the queue is not empty:
        Dequeue a node and call it current
        Add current to result

        For each neighbor in graph[current]:
            If neighbor is not visited:
                Enqueue neighbor
                Mark neighbor as visited

    Return result


'''

def bfs(adj):
    res = []
    queue = []
    queue.append(0)
    visited = [False] * len(adj)
    visited[0] = True

    while queue:
        pop = queue.pop(0)
        res.append(pop)

        for n in adj[pop]:
            if visited[n] == False:
                visited[n] = True
                queue.append(n)

    return n