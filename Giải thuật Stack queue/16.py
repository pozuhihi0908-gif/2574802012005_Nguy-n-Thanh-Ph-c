queue = []

queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

print("Dequeue:", queue.pop(0))

print("Front:", queue[0])

print("Empty:", len(queue) == 0)