import heapq

adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5),(4,8)],
    [(4,3),(5,6)],
    [(5,2)],
    []
]

cost = [2,1,3,2,4,1]

INF = 999999

n = len(adj)

dist = [INF]*n

dist[0] = cost[0]

pq = [(cost[0],0)]

while pq:

    d,u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v,w in adj[u]:

        nd = dist[u] + w + cost[v]

        if nd < dist[v]:

            dist[v] = nd

            heapq.heappush(pq,(nd,v))

print(dist)