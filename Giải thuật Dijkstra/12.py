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

dist1 = [INF] * n
dist1[0] = 0

pq = [(0,0)]

while pq:

    d,u = heapq.heappop(pq)

    if d > dist1[u]:
        continue

    for v,w in adj[u]:

        if dist1[u] + w < dist1[v]:

            dist1[v] = dist1[u] + w
            heapq.heappush(pq,(dist1[v],v))

dist2 = [INF] * n
dist2[2] = 0

pq = [(0,2)]

while pq:

    d,u = heapq.heappop(pq)

    if d > dist2[u]:
        continue

    for v,w in adj[u]:

        if dist2[u] + w < dist2[v]:

            dist2[v] = dist2[u] + w
            heapq.heappush(pq,(dist2[v],v))

print("0 -> 2 =",dist1[2])
print("2 -> 5 =",dist2[5])
print("Tong =",dist1[2]+dist2[5])