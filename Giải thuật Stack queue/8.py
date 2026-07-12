a="3 4 + 2 *"

stack=[]

for x in a.split():

    if x.isdigit():

        stack.append(int(x))

    else:

        b=stack.pop()

        c=stack.pop()

        if x=="+":
            stack.append(c+b)

        if x=="-":
            stack.append(c-b)

        if x=="*":
            stack.append(c*b)

        if x=="/":
            stack.append(c/b)

print(stack.pop())