def dfs(graph, start, visited):
    stack = [start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            print(node, end=' ')
            visited[node] = True
            for neighbor in range(len(graph)):
                if graph[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

top = -1
graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0]
]
stack = [] 
visited = [False] * len(graph)
dfs(graph, 1, visited)
