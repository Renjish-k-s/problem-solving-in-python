graph={}

def add_edge(u,v):
    if u not in graph:
        graph[u]=[]
    graph[u].append(v)

add_edge(0, 1)
add_edge(0, 2)
add_edge(2, 3)
add_edge(3, 4)
add_edge(4, 5)
add_edge(4, 6)
print(graph)



