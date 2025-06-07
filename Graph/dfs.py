'''
Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output: [0, 2, 4, 3, 1]
Explanation: Starting from 0, the DFS traversal proceeds as follows:
Visit 0 → Output: 0 
Visit 2 (the first neighbor of 0) → Output: 0, 2 
Visit 4 (the first neighbor of 2) → Output: 0, 2, 4 
Backtrack to 2, then backtrack to 0, and visit 3 → Output: 0, 2, 4, 3 
Finally, backtrack to 0 and visit 1 → Final Output: 0, 2, 4, 3, 1

----- 
psudo code:

### 2 Args
DFS(graph, start):
    Create an empty list called result
    Create a visited list of size equal to number of vertices, all set to False

    Define a helper function DFS_Visit(node):
        Mark node as visited
        Add node to result

        For each neighbor in graph[node]:
            If neighbor is not visited:
                Call DFS_Visit(neighbor)

    Call DFS_Visit(start)

    Return result


### 1 Arg
DFS(graph):
    Create an empty list called result
    Create a visited list of size equal to number of vertices, all set to False

    Define a helper function DFS_Visit(node):
        Mark node as visited
        Add node to result

        For each neighbor in graph[node]:
            If neighbor is not visited:
                Call DFS_Visit(neighbor)

    Call DFS_Visit(start node, which is 0)

    Return result

'''

def dfs(adj):
    res = []
    visited = [False] * len(adj)
    visited[0] = True

    def helper(node):
        visited[node] = True
        res.append(node)
        for neighbor in adj[node]:
            if visited[neighbor] == False:
                helper(neighbor)

    helper(0)
    return res
