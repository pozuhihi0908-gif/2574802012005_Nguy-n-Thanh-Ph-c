adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5),(4,8)],
    [(4,3),(5,6)],
    [(5,2)],
    []
]

n = len(adj)

INF = 999999

dist = [INF] * n
visited = [False] * n

dist[0] = 0

for i in range(n):

    u = -1

    for j in range(n):
        if visited[j] == False and (u == -1 or dist[j] < dist[u]):
            u = j

    visited[u] = True

    for v, w in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

for i in range(n):
    if dist[i] == INF:
        print(i, ":", -1)
    else:
        print(i, ":", dist[i])