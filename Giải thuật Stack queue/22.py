queue = [1,2,3]

stack = []

while len(queue) > 0:

    stack.append(queue.pop(0))

while len(stack) > 0:

    queue.append(stack.pop())

print(queue)