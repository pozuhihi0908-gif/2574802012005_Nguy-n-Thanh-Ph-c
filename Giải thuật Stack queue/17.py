size = 4

queue = [0] * size

front = 0
rear = -1
count = 0

for x in [1, 2, 3]:

    rear = (rear + 1) % size
    queue[rear] = x
    count += 1

print(queue)

print("Dequeue:", queue[front])

front = (front + 1) % size
count -= 1

rear = (rear + 1) % size
queue[rear] = 4
count += 1

print(queue)