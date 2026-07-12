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

first = [INF]*n
second = [INF]*n

first[0] = 0

pq = [(0,0)]

while pq:

    d,u = heapq.heappop(pq)

    for v,w in adj[u]:

        nd = d + w

        if nd < first[v]:

            second[v] = first[v]
            first[v] = nd

            heapq.heappush(pq,(first[v],v))

        elif nd > first[v] and nd < second[v]:

            second[v] = nd

            heapq.heappush(pq,(second[v],v))

print("Ngan nhat :",first)
print("Ngan nhi :",second)