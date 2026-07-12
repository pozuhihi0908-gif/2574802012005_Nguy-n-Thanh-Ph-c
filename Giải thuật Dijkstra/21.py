import heapq

adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5)],
    []
]

fuel = 5

pq = [(0,0,fuel)]

visited = set()

while pq:

    cost,u,f = heapq.heappop(pq)

    if (u,f) in visited:
        continue

    visited.add((u,f))

    print(u,f,cost)

    for v,w in adj[u]:

        if f >= w:

            heapq.heappush(pq,(cost+w,v,f-w))