queue = []

time = [1,2,3,300,301,302]

for t in time:

    queue.append(t)

    while queue[0] < t-300:

        queue.pop(0)

    print("Time:",t)

    print("Hit:",len(queue))