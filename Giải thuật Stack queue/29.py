queue = [
    ["P1",5],
    ["P2",3],
    ["P3",6]
]

quantum = 2

time = 0

while len(queue) > 0:

    p = queue.pop(0)

    if p[1] <= quantum:

        time += p[1]

        print(p[0],"Hoan thanh luc",time)

    else:

        time += quantum

        p[1] -= quantum

        queue.append(p)