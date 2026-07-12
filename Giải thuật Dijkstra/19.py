import heapq

adj = [
    [(1,0.9),(2,0.5)],
    [(3,0.8)],
    [(3,0.7)],
    []
]

n = len(adj)

best = [0]*n
best[0] = 1

pq = [(-1,0)]

while pq:

    p,u = heapq.heappop(pq)

    p = -p

    if p < best[u]:
        continue

    for v,w in adj[u]:

        np = p*w

        if np > best[v]:

            best[v] = np

            heapq.heappush(pq,(-np,v))

print(best)