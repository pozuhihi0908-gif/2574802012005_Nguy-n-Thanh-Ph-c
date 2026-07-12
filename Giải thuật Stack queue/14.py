price = [100,80,60,70,60,75,85]

stack = []

span = [0]*len(price)

for i in range(len(price)):

    while len(stack)>0 and price[stack[-1]] <= price[i]:

        stack.pop()

    if len(stack)==0:
        span[i]=i+1
    else:
        span[i]=i-stack[-1]

    stack.append(i)

print(span)