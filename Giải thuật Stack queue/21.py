stack1 = []

stack2 = []

stack1.append(1)
stack1.append(2)
stack1.append(3)

if len(stack2) == 0:

    while len(stack1) > 0:

        stack2.append(stack1.pop())

print("Dequeue:", stack2.pop())

print(stack1)

print(stack2)