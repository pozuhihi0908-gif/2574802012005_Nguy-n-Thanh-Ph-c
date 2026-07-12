stack = [3,1,2]

temp = []

while len(stack)>0:

    x = stack.pop()

    while len(temp)>0 and temp[-1] < x:

        stack.append(temp.pop())

    temp.append(x)

while len(temp)>0:

    stack.append(temp.pop())

print(stack)