graph = [
    [1,2],
    [3],
    [3],
    []
]

visited = [False]*4

stack = [0]

while len(stack)>0:

    u = stack.pop()

    if visited[u]:
        continue

    visited[u] = True

    print(u)

    for v in reversed(graph[u]):

        if visited[v] == False:

            stack.append(v)