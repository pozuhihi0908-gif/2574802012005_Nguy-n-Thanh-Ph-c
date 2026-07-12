a = [2,1,3]

n = len(a)

ans = [-1] * n

stack = []

for i in range(n-1,-1,-1):

    while len(stack)>0 and stack[-1] <= a[i]:

        stack.pop()

    if len(stack)>0:

        ans[i]=stack[-1]

    stack.append(a[i])

print(ans)