stack = [1,2,3]

temp = []

print("So phan tu:",len(stack))

while len(stack)>0:

    x=stack.pop()

    print(x)

    temp.append(x)

while len(temp)>0:

    stack.append(temp.pop())

print(stack)