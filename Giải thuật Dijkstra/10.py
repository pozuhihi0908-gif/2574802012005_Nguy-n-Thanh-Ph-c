import heapq

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
dist[0] = 0

pq = []
heapq.heappush(pq, (0, 0))

while pq:

    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v, w in adj[u]:

        if dist[u] + w < dist[v]:

            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

print(dist)