import heapq

adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5),(4,8)],
    [(4,3),(5,6)],
    [(5,2)],
    []
]

INF = 999999

n = len(adj)

dist = [INF] * n
dist[0] = 0

pq = [(0,0)]

while pq:

    d,u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v,w in adj[u]:

        nd = max(dist[u], w)

        if nd < dist[v]:

            dist[v] = nd
            heapq.heappush(pq,(nd,v))

print(dist)