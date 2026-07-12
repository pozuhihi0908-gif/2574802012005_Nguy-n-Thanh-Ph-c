stack=[]

minstack=[]

stack.append(5)
minstack.append(5)

stack.append(3)

if 3<minstack[-1]:
    minstack.append(3)
else:
    minstack.append(minstack[-1])

stack.append(7)

if 7<minstack[-1]:
    minstack.append(7)
else:
    minstack.append(minstack[-1])

print("Min =",minstack[-1])