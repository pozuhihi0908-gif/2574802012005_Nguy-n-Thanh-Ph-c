import heapq

grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

n = len(grid)
m = len(grid[0])

INF = 999999

dist = [[INF]*m for i in range(n)]

dist[0][0] = grid[0][0]

pq = []

heapq.heappush(pq,(grid[0][0],0,0))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while pq:

    d,x,y = heapq.heappop(pq)

    if d > dist[x][y]:
        continue

    for k in range(4):

        nx = x + dx[k]
        ny = y + dy[k]

        if nx>=0 and nx<n and ny>=0 and ny<m:

            nd = dist[x][y] + grid[nx][ny]

            if nd < dist[nx][ny]:

                dist[nx][ny] = nd

                heapq.heappush(pq,(nd,nx,ny))

print(dist[n-1][m-1])