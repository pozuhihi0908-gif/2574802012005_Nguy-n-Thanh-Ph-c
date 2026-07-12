from collections import deque

a = [1,3,-1,-3,5,3]

k = 3

dq = deque()

ans = []

for i in range(len(a)):

    while len(dq) > 0 and dq[0] <= i-k:

        dq.popleft()

    while len(dq) > 0 and a[dq[-1]] <= a[i]:

        dq.pop()

    dq.append(i)

    if i >= k-1:

        ans.append(a[dq[0]])

print(ans)