import heapq

adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5)],
    []
]

k = 2

pq = [(0,0,0)]

while pq:

    d,u,cnt = heapq.heappop(pq)

    print(u,d,cnt)

    if cnt == k:
        continue

    for v,w in adj[u]:

        heapq.heappush(pq,(d+w,v,cnt+1))