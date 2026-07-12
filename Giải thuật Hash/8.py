size = 10

table = [None] * size

def put(x):

    index = x % size

    i = 0

    while table[(index + i * i) % size] != None:
        i = i + 1

    table[(index + i * i) % size] = x

put(10)
put(20)
put(30)
put(40)

print(table)