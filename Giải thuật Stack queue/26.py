queue = []

n = 5

k = 2

for i in range(1,n+1):

    queue.append(i)

while len(queue) > 1:

    for i in range(k-1):

        queue.append(queue.pop(0))

    print("Loai:",queue.pop(0))

print("Song sot:",queue[0])