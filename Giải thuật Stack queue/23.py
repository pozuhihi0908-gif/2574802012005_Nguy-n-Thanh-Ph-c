graph = [
    [1,2],
    [3],
    [3],
    []
]

visited = [False] * 4

queue = []

queue.append(0)

visited[0] = True

while len(queue) > 0:

    u = queue.pop(0)

    print(u)

    for v in graph[u]:

        if visited[v] == False:

            visited[v] = True

            queue.append(v)