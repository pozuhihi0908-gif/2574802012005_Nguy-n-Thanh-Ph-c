import heapq

adj = [
    [(1,4),(2,1)],
    [(3,1)],
    [(1,2),(3,5),(4,8)],
    [(4,3),(5,6)],
    [(5,2)],
    []
]

k = 3

pq = [(0,0)]

count = [0]*6

while pq:

    d,u = heapq.heappop(pq)

    count[u] += 1

    if count[u] > k:
        continue

    print(u,d)

    for v,w in adj[u]:

        heapq.heappush(pq,(d+w,v))